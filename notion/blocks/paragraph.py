from block import NotionBlock
from richtext import RichText


class Paragraph(NotionBlock):
    def __init__(self, text: RichText):
        super().__init__(type="paragraph")
        self.text = text

    def to_dict(self) -> dict:
        return {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": self.text.content,
                            "link": self.text.link
                        }
                    }
                ]
            }
        }