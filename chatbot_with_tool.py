# chatbot_with_tool.py

import google.generativeai as genai
from calculator_tool import safe_calculate
import re
from datetime import datetime

GEMINI_API_KEY = "Insert_your_API_key"  # Replace with your real API key
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def is_math_query(text):
    math_keywords = ['add', 'plus', '+', 'sum', 'subtract', 'minus', '-', 'multiply', '*', 'divide', '/', 'times']
    return any(keyword in text.lower() for keyword in math_keywords)

def get_response(user_input):
    if is_math_query(user_input):
        math_expression = re.findall(r"[0-9+\-*/(). ]+", user_input)
        if math_expression:
            expression = ''.join(math_expression).strip()  # ✅ Join all matched parts
            return safe_calculate(expression)
        else:
            return "❌ Error: Couldn't identify a valid math expression."

    prompt = f"""
Always answer in a step-by-step format.
If the question is a math calculation, say: "I'm using a calculator tool for this."
User: {user_input}
Assistant:"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# ✅ Logging Function
def log_interaction(user_input, assistant_reply):
    with open("level2_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        f.write(f"You: {user_input}\n")
        f.write(f"Assistant: {assistant_reply}\n\n")

# 🟢 Main Loop
print("🤖 Gemini Assistant with Calculator Tool (Level 2)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    reply = get_response(user_input)
    print(f"Assistant: {reply}\n")

    log_interaction(user_input, reply)
