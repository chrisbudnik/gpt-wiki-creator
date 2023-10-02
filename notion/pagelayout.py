from blocks import NotionBlock

class PageLayout:
    def __init__(self, blocks: list[NotionBlock]):
        self.blocks = blocks

    def __repr__(self) -> str:
        pass

    def __hash__(self) -> int:
        pass

    def __eq__(self, o: object) -> bool:
        pass

    def remove(self, index: int) -> None:
        pass

    def insert(self, index: int, block: NotionBlock) -> None:
        pass

    def build(self):
        return {
            "children": [
                block.to_dict() for block in self.blocks
            ]
        }
