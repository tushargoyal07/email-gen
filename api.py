from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key="sk-proj-WJJ2Eqlv9mt1wECfSZQrT3BlbkFJg7mJikxewEyY7S9iOjWb"
)
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "write an email to my boss asking for a raise",
        }
    ],
    model="gpt-3.5-turbo",
)

print(response.choices[0].message)