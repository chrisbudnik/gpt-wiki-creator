from block import NotionBlock


class Breadcrumb(NotionBlock):
    def __init__(self):
        super().__init__(type="breadcrumb")

    def to_dict(self):
        return {
            "object": "block",
            "type": "breadcrumb",
            "breadcrumb": {}
        }