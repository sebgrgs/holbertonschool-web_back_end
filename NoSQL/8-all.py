#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection):
    """ Returns the list of all documents in a collection """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
