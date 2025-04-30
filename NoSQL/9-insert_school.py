#!/usr/bin/env python3
"""insert a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection
    Args:
        mongo_collection: pymongo collection object
        **kwargs: keyword arguments to insert
    Returns:
        The new _id of the inserted document
    """
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
