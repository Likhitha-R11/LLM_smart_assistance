import google.generativeai as genai
import os

# Set your Gemini API key here directly or use an environment variable
GEMINI_API_KEY = "Insert_your_API_key"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


def is_math_question(text):
    math_keywords = ['add', 'plus', '+', 'sum', 'subtract', 'minus', '-', 'multiply', '*', 'divide', '/', 'times']
    return any(keyword in text.lower() for keyword in math_keywords)

def get_response(user_input):
    if is_math_question(user_input):
        return "I'm not allowed to solve math. Please use the calculator tool."

    prompt = f"""
Always answer in a step-by-step format.
User: {user_input}
Assistant:"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def log_interaction(user_input, response):
    with open("interaction_logs.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nAssistant: {response}\n\n")

def main():
    print("🤖 Gemini Smart Assistant (Level 1)\nType 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Assistant: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Assistant: {response}")
        log_interaction(user_input, response)

if __name__ == "__main__":
    main()
