# agent_chatbot.py

import google.generativeai as genai
from calculator_tool import safe_calculate
from translator_tool import translate_text
import re
from datetime import datetime

# 🔑 Paste your API key here
GEMINI_API_KEY = "Insert_your_API_key"  # Example: "AIzaSyD..."
if not GEMINI_API_KEY:
    raise ValueError("❌ Please provide your Gemini API key!")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

def extract_math_expression(text):
    text = text.lower()
    text = text.replace("plus", "+").replace("add", "+")
    text = text.replace("minus", "-").replace("subtract", "-")
    text = text.replace("times", "*").replace("multiply", "*")
    text = text.replace("divided by", "/").replace("divide", "/")
    matches = re.findall(r"[0-9+\-*/(). ]+", text)
    return matches[0].strip() if matches else None

def extract_translation_parts(user_input):
    match = re.search(r"(?:translate\s*)?['\"]?(.*?)['\"]?\s*(?:to|in|into)\s+(\w+)", user_input, re.IGNORECASE)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return None, None

def get_response(user_input):
    responses = []

    # 🔍 Handle translation first
    text, lang = extract_translation_parts(user_input)
    if text and lang:
        translation = translate_text(text, lang)
        responses.append(f"🌍 Translation: {translation}")

    # 🔢 Handle math
    expression = extract_math_expression(user_input)
    if expression:
        result = safe_calculate(expression)
        if "Error" in result:
            responses.append(f"❌ Math Error: {result}")
        else:
            responses.append(result)

    # 💬 If neither worked, use Gemini LLM
    if not responses:
        prompt = f"""
Always explain your reasoning step-by-step.
If the user asked a math or translation question, say: "I'm using a special tool for this."
User: {user_input}
Assistant:"""
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {e}"

    return "\n".join(responses)

# 📝 Logging (Optional, for Level 3 Logs)
def log_interaction(user_input, assistant_reply):
    with open("level3_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        f.write(f"You: {user_input}\n")
        f.write(f"Assistant: {assistant_reply}\n\n")

# ▶️ CLI Loop
print("🤖 Gemini Multi-Tool Assistant (Level 3)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    reply = get_response(user_input)
    print(f"Assistant: {reply}\n")
    log_interaction(user_input, reply)
