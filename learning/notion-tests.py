import requests


NOTION_TOKEN = ""
DATABASE_ID = ""

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_pages(num_pages=None):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    import json
    with open('db.json', 'w', encoding='utf8') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    
    # while data["has_more"] and get_all:
    #     payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
    #     url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    #     response = requests.post(url, json=payload, headers=headers)
    #     data = response.json()
    #     results.extend(data["results"])
    return results


#print(get_pages())


def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res



wiki = "Test Title - intro4"
tags = "intro"
data = {
    "wiki": {"title": [{"text": {"content": wiki}}]},
    "tags": {"rich_text": [{"text": {"content": tags}}]},
    "level": {"multi_select": [{"name": tags}]}
}

response = create_page(data)
page_block_id = response.json()["id"]

#'8117715a-0ca3-4c3b-8965-fae2ab3eddc6'

def edit_page(page_block_id, data: dict):
    edit_url = f"https://api.notion.com/v1/blocks/{page_block_id}/children"
    res = requests.patch(edit_url, headers=headers, json=data)
    if res.status_code == 200:
        print(f"{res.status_code}: Page edited successfully")
    else:
        print(f"{res.status_code}: Error during page editing")
    return res

text_content = """
some text to check if this works fine hahaha
"""

code = """conda config --add channels channel_name"""

bullet_point1 = "bullet point - only one?"

callout = "This is superstar callout"

blocks = {
    "children": [
        #breadcrumb
        {
        "object": "block",
        "type": "breadcrumb",
        "breadcrumb": {}
        },
        # paragraph
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                    
                    "type": "text",
                    "text": {
                        "content": "This is an ",
                        "link": None
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "This is an ",
                    "href": None
                    
                    }
                ]
            },
        },

        # code block
        {
        "object": "block",
        "type": "code",
        "code": {
            "caption": [],
                "rich_text": [{
            "type": "text",
            "text": {
                "content": code
            }
            }],
            "language": "bash"
        }
        },
        # bullet points
        {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [
            {
            "type": "text",
            "text": {
                "content": bullet_point1,
                "link": None
            }
            }
            ],
            "color": "default",
            
        }
        },
        {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [
            {
            "type": "text",
            "text": {
                "content": bullet_point1 + "__ must be 2",
                "link": None
            }
            }
            ],
            "color": "default",
            
        }
        },
        # callout
        {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{
            "type": "text",
            "text": {
                "content": callout,
                "link": None
            }
            }],
            "icon": {
            "emoji": "⭐"
            },
            "color": "default"
        }
        }
    ]
}