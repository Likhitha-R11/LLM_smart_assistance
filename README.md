# LLM_smart_assistance
A Gemini-powered intelligent assistant that can understand natural language queries and respond using multiple tools like Calculator-solve math expressions, Translator — Translates text, LLM Agent — Answers queries using Google Gemini.  This project demonstrates multi-intent detection and tool invocation using Python and Google’s Generative AI API.
- ✅ **Level 1**: Simple LLM chatbot using Gemini API
- ✅ **Level 2**: Math Assistant (uses a secure calculator tool for expressions like 23 + 7)
- ✅ **Level 3**: Multi-intent Assistant (handles both "translation" and "math" in the same query)

## 💡 Features

- Uses **Google Generative AI (Gemini)** for intelligent replies
- Can **calculate** math expressions safely
- Can **translate** phrases between languages (using `googletrans`)
- Supports **multi-intent detection** (Level 3)


## Repository Structure
LLM_smart_assistance/
│
├── agent_chatbot.py         # Level 3: Multi-tool assistant (math + translation)
├── chatbot.py               # Level 1: Basic Gemini chatbot
├── chatbot_with_tool.py     # Level 2: Gemini chatbot with calculator
│
├── calculator_tool.py       # Math expression evaluator
├── translator_tool.py       # Translator using googletrans
│
├── level2_log.txt           # Interaction log for Level 2
├── level3_log.txt           # Interaction log for Level 3
├── interaction_logs/        # Folder containing Level 1 interactions (if separate)
│
├── .env                     # (Not committed) Stores your API key securely
├── .gitignore               # Specifies files/folders to ignore in Git
├── README.md                # Project overview and instructions
└── requirements.txt         # (Optional) List of dependencies

## 🚀 How to Run

### 1. Ensure Python 3.11 is Installed

This project requires **Python 3.11** due to compatibility issues with some libraries.

- Download Python 3.11:  
  👉 [https://www.python.org/downloads/release/python-3110/](https://www.python.org/downloads/release/python-3110/)

- During installation:
  - ✅ Check **"Add Python to PATH"**
  - ✅ Enable `pip`

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python3.11 -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On Mac/Linux

3. Install required packages:

   ```bash
   pip install google-generativeai googletrans==4.0.0-rc1
4.Create a .env file in your project folder and add your API key:
  GEMINI_API_KEY=your_actual_gemini_api_key_here
5.Run the assistant for each level:

- ✅ Level 1:
  python chatbot.py

- ✅ Level 2:
  python chatbot_with_tool.py

- ✅ Level 3:
  python agent_chatbot.py


## 🛠️ Tech Stack

- Python 3.11
- Google Generative AI API (Gemini)
- googletrans 4.0.0-rc1
- re, dotenv, ast (built-in modules)

> ⚠️ **Note:** Make sure your API key is stored securely in a `.env` file and never shared publicly. Use `.gitignore` to avoid uploading sensitive info.

### 👩‍💻 Author

Ragam Likhitha  
[🔗 LinkedIn](https://www.linkedin.com/in/ragam-likhitha-2b84462bb)




