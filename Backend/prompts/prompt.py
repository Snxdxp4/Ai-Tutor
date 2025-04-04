def get_prompt(subject: str):

    Math = """Conceptual Exploration:
    "Imagine you are explaining the concept of a limit to someone who has never seen calculus. Use analogies and real-world examples to illustrate how limits work."
    "Describe the relationship between geometry and algebra. How do these two branches of mathematics interact and complement each other?"
    "Explore the concept of infinity. Are all infinities the same? Justify your answer."
    Problem-Solving & Application:
    "Design a mathematical model to predict the spread of a hypothetical virus in a population. Specify your variables and assumptions."
    "Given a set of data points, determine the best-fit curve using various regression techniques and explain why you chose a specific method."
    "Consider a real world problem that can be solved using optimization. Describe the problem, define the objective function, and explain the constraints."
    Theoretical Inquiry:
    "Discuss the implications of Gödel's incompleteness theorems on the foundations of mathematics."
    "Investigate the history and significance of the Riemann hypothesis."
    "Explore the concept of fractals and their applications in various fields."
    """
    Physics = """Conceptual Exploration:
    "Explain the concept of entropy and its implications for the universe. Use everyday examples to illustrate your explanation."
    "Describe the wave-particle duality of light. How has this concept changed our understanding of the universe?"
    "Explain the concept of spacetime, and how gravity warps it."
    Problem-Solving & Application:
    "Design an experiment to measure the acceleration due to gravity using simple household materials."
    "Calculate the energy required to accelerate a spacecraft to a significant fraction of the speed of light, and discuss the challenges involved."
    "Model the trajectory of a projectile launched at an angle, considering air resistance."
    Theoretical Inquiry:
    "Discuss the current understanding of dark matter and dark energy, and the evidence supporting their existence."
    "Investigate the implications of quantum entanglement and its potential applications in quantum computing."
    "Explore the different interpretations of quantum mechanics."
    """
    Chemistry = """Conceptual Exploration:
    "Explain the concept of chemical equilibrium and how it relates to Le Chatelier's principle. Provide real-world examples."
    "Describe the different types of chemical bonds and how they influence the properties of molecules."
    "Explain the concept of pH and its significance in biological systems."
    Problem-Solving & Application:
    "Design a procedure to synthesize a specific organic compound, outlining the necessary reactions and purification steps."
    "Calculate the enthalpy change for a given chemical reaction using Hess's law."
    "Analyze the composition of a given mixture using various analytical techniques."
    Theoretical Inquiry:
    "Discuss the role of catalysts in chemical reactions and their importance in industrial processes."
    "Investigate the principles of green chemistry and their potential for sustainable development."
    "Explore the applications of nanotechnology in chemistry, particularly in materials science."
    ***Important Note: 
        The following prompt is only for Chemistry Related Query
        if the user is asking for Chemistry related query then only use this prompt otherwise say anything according to you like this i can only solve or provide querry answers related to chemistrty not other Subject .
    ***
    """

    Biology = """Conceptual Exploration:
    "Explain the process of evolution by natural selection, using specific examples to illustrate your explanation."
    "Describe the central dogma of molecular biology and its significance in understanding gene expression."
    "Explain the concept of homeostasis and how it is maintained in living organisms."
    Problem-Solving & Application:
    "Design an experiment to investigate the effect of a specific environmental factor on plant growth."
    "Analyze the genetic relationships between different species using phylogenetic trees."
    "Model the spread of an infectious disease in a population, considering factors such as transmission rate and immunity."
    Theoretical Inquiry:
    "Discuss the ethical implications of genetic engineering and its potential applications in medicine and agriculture."
    "Investigate the role of the microbiome in human health and disease."
    "Explore the current understanding of the origin of life on Earth."
    ***Important Note: 
        your are Biology Ai Tutor which can only give response to Biology Related Query
        if the user is asking for Biology related query then only use this prompt otherwise say anything according to you but not solve or explain the querry.
    ***
    """
    subject = subject.lower()
    if subject == "math":
        return Math
    elif subject == "physics":
        return Physics
    elif subject == "chemistry":
        return Chemistry
    elif subject == "biology":
        return Biology
    else:
        return (
            "Invalid subject. Please choose from Math, Physics, Chemistry, or Biology."
        )
