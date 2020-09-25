import pandas as pd
from .scrapper import get_item_name


def create_item_json(item_id, dataframe):
    """
    Method to create a given item a dict structure to return the JSON
    Args:
        item_id(int): Given Item id
        dataframe: pandas dataframe with hole dataset

    Returns:

    """
    row = dataframe[dataframe['id'] == item_id]

    return_dict = {'id': item_id, 'name': get_item_name(item_id=item_id), 'enhancement': float(row['enhancement']),
                   'maximum': float(row['maximum']), 'minimum': float(row['minimum']), 'price': float(row['price']),
                   'count': float(row['count'])}
    return True, return_dict
