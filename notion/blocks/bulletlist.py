from typing import List
from block import NotionBlock
from richtext import RichText


class BulletList(NotionBlock):
    def __init__(self, points: List[RichText], color="default"):
        self.points = points
        self.color = color

    def to_dict(self) -> dict:
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