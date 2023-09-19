from abc import ABC, abstractmethod


class NotionBlock(ABC):
    """Base class for all Notion blocks."""

    def __init__(self, type: str):
        self.type = type

    @abstractmethod
    def to_dict(self) -> dict:
        """Converts the Notion block into dict."""
        pass