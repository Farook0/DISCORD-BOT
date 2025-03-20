import os
from dotenv import load_dotenv
import groq

load_dotenv()

# Load API Key from .env
groq_api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Groq client
groq_client = groq.Groq(api_key=groq_api_key)

# Store chat history
chat_history = []

def mistral_response(prompt):
    global chat_history

    if prompt.lower() == "clear the chat":
        chat_history = []  # Clear chat history
        return "Chat history cleared."

    chat_history.append({"role": "user", "content": prompt})

    response = groq_client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=chat_history,
        max_tokens=100
    )
    
    # Extract response properly
    if response.choices and len(response.choices) > 0:
        bot_response = response.choices[0].message.content.strip()
        chat_history.append({"role": "assistant", "content": bot_response})
        return bot_response

    return "No response received."

# Example usage
print(mistral_response("Hello, how are you?"))
print(mistral_response("clear the chat"))  # This will clear the chat
print(mistral_response("What is AI?"))  # Starts a new conversation
