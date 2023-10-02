from block import NotionBlock
from richtext import RichText


class Code(NotionBlock):
    def __init__(self, text: RichText, language: str):
        super().__init__(type="code")
        self.text = text
        self.language = language

    def to_dict(self) -> dict:
        return {
            "object": "block",
            "type": "code",
            "code": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": self.text.content
                        }
                    }
                ],
                "language": self.language
            }
        }