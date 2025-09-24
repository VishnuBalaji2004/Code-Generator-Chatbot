Code Generator Chatbot 🤖
This repository contains the source code for an AI-powered Code Generator Chatbot. The application provides a simple and interactive web interface where users can specify a programming language and a problem statement to receive instant, high-quality code solutions.

This project is built using a modern stack, leveraging the Groq API for ultra-fast LLM inference, LangChain for robust prompt and model orchestration, and Streamlit for the user interface.

✨ Key Features

⚡ High-Speed Generation: Utilizes the Groq API with the llama-3.1-8b-instant model for near-instantaneous code generation.

🖥️ Interactive Web UI: A clean and user-friendly interface built with Streamlit.

🔗 Powered by LangChain: Employs the LangChain framework to structure the logic, manage prompts, and interface with the LLM.

🎯 Precise & Guardrailed Responses: Implements a sophisticated system prompt to ensure the chatbot stays on task, rejects non-coding requests, and produces clean, syntax-correct code.

🔍 Traceable with LangSmith: Integrated with LangSmith for full visibility and debugging of the LLM chain.

🛠️ Tech Stack
Frontend: Streamlit

LLM Orchestration: LangChain

LLM Provider: Groq

Language: Python

Observability: LangSmith

🚀 Getting Started
Follow these instructions to download and run the project on your local machine.

Prerequisites
Python 3.11 (This project was built and tested with this version).

1. Download and Unzip the Project Files
First, you need to download the project files directly from this page.

At the top of the repository page, click the green < > Code button.

In the dropdown menu, select Download ZIP.

Find the downloaded .zip file on your computer and unzip it to a location you can easily access (like your Desktop or Documents folder).

2. Open a Terminal in the Project Folder
After unzipping the file, you need to open a command prompt or terminal and navigate into the project directory.

Bash

# Example: If you unzipped it on your Desktop
cd Desktop/Code-Generator-Chatbot-main
3. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies and avoid conflicts.

Bash

# Create the virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
4. Install Dependencies
Install all the required packages using the 

requirements.txt file.

Bash

pip install -r requirements.txt
5. Configure Environment Variables
You must provide your own API keys for the application to work.

In the project folder, create a new file named .env.

Open the .env file and paste the following content. You must replace the placeholder text with your own secret keys.

Code snippet

# Get your Groq API Key from https://console.groq.com/keys
GROQ_API_KEY="YOUR_GROQ_API_KEY_HERE"

# Optional: For LangSmith tracing, get your keys from https://smith.langchain.com/
LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="YOUR_LANGSMITH_API_KEY_HERE"
LANGSMITH_PROJECT="Code Generator"
Important: The GROQ_API_KEY is mandatory to run the application. The LANGSMITH variables are optional.

6. Run the Application
Now you are ready to run the Streamlit application.

Bash

streamlit run app.py
Your web browser should automatically open with the Code Generator Bot interface.

🔧 Troubleshooting
Model Not Working or Deprecated
The model specified in the code (

llama-3.1-8b-instant) might become outdated over time. If you encounter errors related to the model, follow these steps:

Check for available models: Visit the GroqCloud Models page to see the list of currently supported models.

Update the model name:

Open the 

model.py file.

Find the line that specifies the model name:

Python

return ChatGroq(
    model="llama-3.1-8b-instant",  # <-- CHANGE THIS LINE
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
    )
Replace "llama-3.1-8b-instant" with a new, valid model name from the Groq documentation.

Save the file and restart the Streamlit application.