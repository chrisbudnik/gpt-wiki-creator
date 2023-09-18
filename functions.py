import openai 
from openai.openai_object import OpenAIObject
from typing import Literal


def _process_chat_response(response: OpenAIObject) -> str:
    """Processes openai chat response and saves message output as string."""

    response_dict: dict = response.to_dict_recursive()
    response_choice: dict[str: dict] = response_dict.get("choices", {})[0]
    return response_choice.get("message", {}).get("content", None)

def get_chat_response(context: str, prompt: str, **kwargs):
    """Query openai api for chat response based on provided context, prompt and extra kwargs."""

    response: OpenAIObject = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ],
        **kwargs
        )
    return _process_chat_response(response)

def save_to_file(content: str, filename: str, extension: Literal["txt", "md"]) -> None:
    """Saves content into markdown file."""

    with open(f"{filename}.{extension}", "w") as file:
        file.write(content)

def read_txt_to_string(txt_filename: str) -> str:
    with open(txt_filename, 'r') as txt_file:
        content = txt_file.read()
    return content