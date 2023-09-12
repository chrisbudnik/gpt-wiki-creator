import openai 
from openai.openai_object import OpenAIObject

def get_chat_response(context: str, prompt: str, **kwargs):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ],
        **kwargs
        )
    response_dict = response.to_dict_recursive()
    return response_dict.get("choices", {})[0].get("message", {}).get("content", None)

