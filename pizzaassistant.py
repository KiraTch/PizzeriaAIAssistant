import os, time
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig

# Load env
load_dotenv()

# Initialize client
client = genai.Client()

MODEL = "gemini-2.0-flash"

# Conversation history
history = [
    {"role": "system", "content": """
    You are a friendly and knowledgeable virtual assistant working at a cozy neighborhood pizzeria. pizzeria called kira

    Your job is to help customers:
    - Choose the perfect pizza based on their preferences (ingredients, dietary needs, size, price etc.).
    - Suggest popular or seasonal options if they are unsure.
    - Recommend complementary sides or drinks.
    - Be polite, enthusiastic, and helpful in every reply.
    - Keep responses short, clear, and conversational.
    MOST IMPORTANT:
    - if the user's response is not about pizzas, switch the conversation politely back to pizzas and refuse to respond.
    Do not break character or mention being an AI.
    """}

]

def ask_agent(user_input, retries=3):
    history.append({"role": "user", "content": user_input})
    for i in range(retries):
        try:
            resp = client.models.generate_content(
                model=MODEL,
                contents=[msg["content"] for msg in history],
                config=GenerateContentConfig(response_modalities=["TEXT"])
            )
            text = resp.text.strip()
            history.append({"role": "assistant", "content": text})
            return text
        except genai.Error as e:
            print(f"ServerError: {e} (retry {i + 1}/{retries})")
            time.sleep(1)
    return "Sorry, I’m having trouble connecting right now."

def main():
    print("Welcome to PizzaBot! Type 'exit' to stop.\n")
    while True:
        u = input("You: ").strip()
        if u.lower() in ("exit","quit"):
            print("Agent: Have a cheesy day! 🍕")
            break
        reply = ask_agent(u)
        print(f"Agent: {reply}\n")

if __name__ == "__main__":
    main()