#import the OpenAI library
import os
from openai import OpenAI
from dotenv import load_dotenv

#load the API key from the .env file
load_dotenv()  

#set the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

#create a new client
client = OpenAI(api_key=api_key)

#create a new chat completion
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)

#print the response
print(response.choices[0].message.content)