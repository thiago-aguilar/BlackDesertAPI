import pandas as pd
from .scrapper import get_item_name
import numpy as np


def create_item_json(item_id, dataframe, item_enhancement, async_flag=False):
    """
    Method to create a given item a dict structure to return the JSON
    Args:
        item_id(int): Given Item id
        dataframe: pandas dataframe with hole dataset

    Returns:

    """
    row = dataframe[np.logical_and((dataframe['id'] == item_id),(dataframe['enhancement'] == item_enhancement))]
    if len(row) == 0:
        return False,{}

    if not async_flag:
        return_dict = {'id': item_id, 'name': get_item_name(item_id=item_id), 'enhancement': float(row['enhancement']),
                       'maximum': float(row['maximum']), 'minimum': float(row['minimum']), 'price': float(row['price']),
                       'count': float(row['count'])}

    else:
        return_dict = {'id': item_id, 'name':str(row['name']._values[0]), 'enhancement': float(row['enhancement']),
                       'maximum': float(row['maximum']), 'minimum': float(row['minimum']), 'price': float(row['price']),
                       'count': float(row['count'])}

    return True, return_dict

