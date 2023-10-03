

class BlockInstrictions:
    """Converts markdown to Notion block instructions"""
    
    def __init__(self, markdown: str):
        self.markdown = markdown
        self.instruction = {}