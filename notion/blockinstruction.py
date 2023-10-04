
# prompt
prompt = """become a markdown converter. the convertion looks like this: translate md formatting 
into list of python dicts in this format {name: name_of_formatting, text: value}. 
this means when provided a md header like this: ### Heading 3 the answer shoud be [{"name": "H3", "test": "Heading 3"}] """


class BlockInstrictions:
    """Converts markdown to Notion block instructions"""

    def __init__(self, markdown: str):
        self.markdown = markdown
        self.instruction = {}
