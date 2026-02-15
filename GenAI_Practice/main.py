from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=API_KEY)

chat = client.chats.create(
        model="gemini-2.5-flash",
        config={
            'temperature': 0,
            'max_output_tokens': 500,
        },
        ) 

while True:
    query = input("📝 Enter your query: ")

    if query.lower() in ['bye']:
        print("Exiting the program. Goodbye!")
        break

       
    response = chat.send_message(query)

    print("🤖 Response:- ",response.text)