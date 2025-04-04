from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from flask_cors import CORS
from pymongo import MongoClient
from google import genai
from prompts.prompt import get_prompt
from models.student_model import StudentLevelPredictor
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

load_dotenv()

print(os.getenv("GEMINI_API_KEY"))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# MongoDB setup
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['ai_tutor']
users = db['users']

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session management
CORS(app)

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user'] = {
                'id': str(user['_id']),
                'name': user['name'],
                'email': user['email']
            }
            flash('Successfully logged in!', 'success')
            return redirect(url_for('dashboard'))
        
        flash('Invalid email or password.', 'error')
    return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('register.html')
        
        if users.find_one({'email': email}):
            flash('Email already registered.', 'error')
            return render_template('register.html')
        
        hashed_password = generate_password_hash(password)
        user_data = {
            'name': name,
            'email': email,
            'password': hashed_password
        }
        users.insert_one(user_data)
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route("/logout")
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route("/api/generate", methods=["POST"])
@login_required
def generate():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    tutor = data.get("tutor")
    system_prompt = get_prompt(tutor)
    if not tutor:
        return jsonify({"error": "No tutor provided"}), 400
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Combine system prompt and user prompt
    combined_prompt = f"System Instructions:\n{system_prompt}\n\nUser Question: {prompt}"

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[combined_prompt],
        )
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/api/predict-level", methods=["POST"])
@login_required
def predict_level():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    knowledge_level = data.get("knowledge_level")
    learning_speed = data.get("learning_speed")
    
    if not knowledge_level or not learning_speed:
        return jsonify({"error": "Knowledge level and learning speed are required"}), 400
    
    try:
        predictor = StudentLevelPredictor()
        result = predictor.predict_level(knowledge_level, learning_speed)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)