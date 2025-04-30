#!/usr/bin/env python3
"""changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name: string representing the school name to update
        topics: list of topics approached in the school
    """
    if mongo_collection is None:
        return
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
