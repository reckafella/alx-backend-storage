#!/usr/bin/env python3
'''
Module contains a Python function that lists all documents in a collection
'''


def list_all(mongo_collection):
    '''
    Python function that lists all documents in a collection
    '''
    documents = []
    result = mongo_collection.find()
    for document in result:
        documents.append(document)
    return documents
