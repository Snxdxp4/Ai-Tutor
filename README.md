v# AI Tutor Project

A modern web application that provides AI-powered tutoring assistance across multiple subjects. The application features a personalized learning experience with level prediction and interactive chat interface.

## Features

- 🤖 AI-powered tutoring across multiple subjects
- 📊 Student level prediction based on knowledge and learning speed
- 💬 Modern chat interface with real-time responses
- 🎯 Subject-specific tutoring (Math, Physics, Chemistry, Biology)
- 📱 Responsive design for all devices
- 🔒 Secure user authentication

## Demo Video

Watch our project demo to see the AI Tutor in action:

[AI Tutor Demo](Demo.mp4)

## Tech Stack

### Frontend

- HTML5
- Tailwind CSS
- JavaScript (Vanilla)

### Backend

- Python
- Flask
- MongoDB
- XGBoost
- Scikit-learn
- Google Gemini AI

## Project Structure

```
Intel-Project/
├── Backend/
│   ├── models/
│   │   ├── student_model.py
│   │   ├── xgboost_model.joblib
│   │   ├── scaler.joblib
│   │   ├── label_encoders.joblib
│   │   └── features.joblib
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── index.html
│   ├── static/
│   │   └── css/
│   └── app.py
├── Data/
│   └── intel.csv
└── README.md
```

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone [repository-url]
   cd Intel-Project
   ```

2. **Set up Python virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install system dependencies**

   - For Windows: Install [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
   - For Mac: `brew install libomp`
   - For Linux: `sudo apt-get install libgomp1`

5. **Set up environment variables**
   Create a `.env` file in the Backend directory:

   ```
   GEMINI_API_KEY=your_api_key_here
   MONGODB_URI=mongodb://localhost:27017/
   ```

6. **Initialize MongoDB**

   - Install MongoDB
   - Start MongoDB service
   - Create database: `ai_tutor`

7. **Run the application**
   ```bash
   cd Backend
   python app.py
   ```

## API Endpoints

### Authentication

- `POST /register` - Register new user
- `POST /login` - User login
- `GET /logout` - User logout

### AI Tutor

- `POST /api/generate` - Generate AI tutor response
- `POST /api/predict-level` - Predict student level

## Model Details

The student level prediction model uses:

- XGBoost classifier
- Features: Knowledge Level, Learning Speed
- Label encoding for categorical variables
- Standard scaling for numerical features

## License

This project is licensed under the MIT License - see the LICENSE file for details.
