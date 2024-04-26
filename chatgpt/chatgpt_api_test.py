from pprint import pprint
import os
from openai import OpenAI

api_key = 'your api key'
client = OpenAI(api_key=api_key)

# gpt-3.5-turbo-1106 : 1K 토큰당 0.001달러
# gpt-3.5-turbo-0125 : 1M 토큰당 0.500달러 
model = "gpt-3.5-turbo-0125"  

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Who won the world series in 2020?"}
]

response = client.chat.completions.create(model=model, messages=messages).model_dump()

pprint(response)
