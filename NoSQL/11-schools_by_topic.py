#!/usr/bin/env python3
"""return the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic: string representing the topic searched
    Returns:
        list of school having the topic
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({"topics": topic}))
