#!/usr/bin/env python3
'''
Module contains a class to store an instance of the Redis client
'''
import redis
import uuid


class Cache:
    '''
    stores an instance of the Redis client
    '''
    def __init__(self) -> None:
        '''
        stores an instance of the Redis client in _redis
        '''
        self.__redis: redis.Redis = redis.Redis()
        self.__redis.flushdb(asynchronous=True)

    def store(self, data: str | bytes | int | float) -> str:
        '''
        takes a data argument and returns a string
        generates a random key using uuid, stores the input data in Redis\
            using the random key and return the key
        '''
        self._key: uuid.uuid1 = str(uuid.uuid1())
        self.__redis.set(self._key, data)
        return self._key
