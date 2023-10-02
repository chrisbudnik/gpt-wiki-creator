from block import NotionBlock


class Breadcrumb(NotionBlock):
    def __init__(self) -> None:
        super().__init__(type="breadcrumb")

    def to_dict(self) -> dict:
        return {
            "object": "block",
            "type": "breadcrumb",
            "breadcrumb": {}
        }