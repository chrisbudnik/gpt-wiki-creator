from typing import List, Union

class RichText:
    def __init__(self, content: str, link=None):
        self.content = content
        self.link = link

class Block:
    def to_dict(self):
        raise NotImplementedError()

class Breadcrumb(Block):
    def to_dict(self):
        return {
            "object": "block",
            "type": "breadcrumb",
            "breadcrumb": {}
        }

class Paragraph(Block):
    def __init__(self, text: RichText):
        self.text = text

    def to_dict(self):
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

class Code(Block):
    def __init__(self, text: RichText, language: str):
        self.text = text
        self.language = language

    def to_dict(self):
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

class BulletList(Block):
    def __init__(self, points: List[RichText], color="default"):
        self.points = points
        self.color = color

    def to_dict(self):
        return [
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": point.content,
                                "link": point.link
                            }
                        }
                    ],
                    "color": self.color,
                }
            }
            for point in self.points
        ]

class Callout(Block):
    def __init__(self, text: RichText, icon: str):
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

# Example usage
blocks = [
    Breadcrumb(),
    Paragraph(text=RichText("This is an example paragraph")),
    Code(text=RichText("echo 'Hello World!'"), language="bash"),
    BulletList(points=[RichText("Point 1"), RichText("Point 2")]),
    Callout(text=RichText("This is a callout"), icon="⭐")
]

block_dicts = [block.to_dict() for block in blocks]

# Handle BulletList separately as it returns a list of dictionaries
final_block_dicts = []
for block_dict in block_dicts:
    if isinstance(block_dict, list):
        final_block_dicts.extend(block_dict)
    else:
        final_block_dicts.append(block_dict)

print(final_block_dicts)
