import re

def markdown_to_json(md_text):
    result = []
    
    # Split the text into lines
    lines = md_text.strip().split("\n")
    
    for line in lines:
        if line.startswith("# "):
            result.append({"h1": line[2:].strip()})
        elif line.startswith("## "):
            result.append({"h2": line[3:].strip()})
        elif line.startswith("### "):
            result.append({"h3": line[4:].strip()})
        elif line.startswith("#### "):
            result.append({"h4": line[5:].strip()})
        elif line.startswith("##### "):
            result.append({"h5": line[6:].strip()})
        elif line.startswith("###### "):
            result.append({"h6": line[7:].strip()})
        elif line.startswith("```"):
            continue  # Ignore code block delimiters for this example
        elif line.startswith("- ") or line.startswith("* "):
            result.append({"list_item": line[2:].strip()})
        elif re.match(r'^\d+\.', line):
            result.append({"ordered_list_item": re.sub(r'^\d+\.', '', line).strip()})
        else:
            result.append({"paragraph": line.strip()})
    
    return result

# Sample Markdown text
md_text = """# Advanced Conda Configuration Options

In this section, we will explore advanced configuration options for managing miniconda environments on macOS. These options will enable you to fine-tune your conda setup and enhance your development experience.

## 1. Creating an environment from a specific channel

By default, conda will search for packages in the default channel. However, you can create an environment and specify a specific channel to install packages from. To do this, use the following command:

```bash
conda create -n env_name -c channel_name python=3.8
````
"""
print(markdown_to_json(md_text))