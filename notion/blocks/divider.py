from block import NotionBlock


class Divider(NotionBlock):
    def __init__(self) -> None:
        super().__init__(type="divider")

    def to_dict(self) -> dict:
        return {
            
        }