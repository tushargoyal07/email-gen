from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api)

email_type = input("What type of email do you want to write? ")
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a expert in writing an email, whatever kind of email it is, you can write it in a professional way and make it look good and original giving it a little human touch.",
        },
        {
            "role": "user",
            "content": f"I need to write an email of {email_type}",
        }
    ],
    model="gpt-3.5-turbo",
)

print(response.choices[0].message)