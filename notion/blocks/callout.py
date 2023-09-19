from block import NotionBlock
from richtext import RichText


class Callout(NotionBlock):
    def __init__(self, text: RichText, icon: str):
        super().__init__(type="callout")
        self.text = text
        self.icon = icon

    def to_dict(self):
        return {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": self.text.content,
                            "link": self.text.link
                        }
                    }
                ],
                "icon": {
                    "emoji": self.icon
                },
            }
        }