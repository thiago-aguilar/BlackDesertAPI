from lxml import html
import requests
import time


def get_item_name(item_id: str):
    """
    Function to scrap from the internet the portuguese name of a given item_id
    Args:
        item_id(str): Given item id

    Returns:
        item_name(str): Portuguese name scrapped from the brazilian website

    """
    url = f'https://bdocodex.com/pt/item/{item_id}/'

    page = ''
    while page == '':
        try:
            page = requests.get(url)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            continue
    tree = html.fromstring(page.content)

    if len(tree.xpath('//*[@id=\"item_name\"]')) > 0:
        item_name = tree.xpath('//*[@id=\"item_name\"]')[0].text_content()
        item_name = str(item_name)

        return item_name

    else:
        return False
