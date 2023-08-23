import os
from pprint import pprint
import openai 
from openai.openai_object import OpenAIObject

# setup api key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# response
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "what is the step-by-step guide to learning cmd (mac)"},
  ],
  temperature=0,
  max_tokens=1024
)

def get_message(res: OpenAIObject) -> str:
    response_dict = res.to_dict_recursive()
    return response_dict.get("choices", {})[0].get("message", {}).get("content", None)

text = get_message(response)
pprint(text)
# print(response[0].get("choices", {}).get("message", {}).get("content", None))