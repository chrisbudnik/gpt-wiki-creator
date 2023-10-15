
# prompt
prompt = """become a markdown converter. the convertion looks like this: translate md formatting 
into list of python dicts in this format {name: name_of_formatting, text: value}. 
this means when provided a md header like this: ### Heading 3 the answer shoud be [{"name": "H3", "test": "Heading 3"}] """

"""
become a markdown converter. the convertion looks like this: 
translate md formatted string into a list of python dicts in this format {name: name_of_formatting, text: value}.  this means when provided a md header like this: ### Heading 3 the answer shoud be [{"name": "H3", "text": "Heading 3"}]
other cases:
Headings: {'h1': 'text'}, {'h2': 'text'}, etc.
Code blocks: {'code': 'content'}.
Bullet points: {'bullet': 'text'}.
Tables: {'table': {'Header 1': 'Data 1', 'Header 2': 'Data 2'}} (assuming 1 row for simplicity; you can extend it for multiple rows).
Callouts: {'callout': 'text'}.
"""

class BlockInstrictions:
    """Converts markdown to Notion block instructions"""

    def __init__(self, markdown: str):
        self.markdown = markdown
        self.instruction = {}
