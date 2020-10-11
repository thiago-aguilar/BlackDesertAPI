from lxml import html
import requests


def get_item_name(item_id: str):
    """
    Function to scrap from the internet the portuguese name of a given item_id
    Args:
        item_id(str): Given item id

    Returns:
        item_name(str): Portuguese name scrapped from the brazilian website

    """
    url = f'https://bdocodex.com/pt/item/{item_id}/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    if len(tree.xpath('//*[@id=\"item_name\"]')) > 0:
        item_name = tree.xpath('//*[@id=\"item_name\"]')[0].text_content()
        item_name = str(item_name)

        return item_name

    else:
        return False
