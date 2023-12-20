#!/usr/bin/env python3
'''
Module contains a class to store an instance of the Redis client
'''
import redis
import uuid
from typing import Union, Callable


class Cache:
    '''
    stores an instance of the Redis client
    '''
    def __init__(self) -> None:
        '''
        stores an instance of the Redis client in _redis
        '''
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb(asynchronous=True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        takes a data argument and returns a string
        generates a random key using uuid, stores the input data in Redis\
            using the random key and return the key
        '''
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) ->\
            Union[str, bytes, int, float, list]:
        '''
        method that take a key string argument and an optional Callable\
            argument named fn. This callable will be used to convert the\
                data back to the desired format.
        '''
        result = self._redis.get(key)
        return fn(result) if result else None

    def get_str(self, data: bytes) -> str:
        '''
        returns a string representation of data received from redis
        '''
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        '''
        return integer representation of data received from redis
        '''
        return int(self.get_str(data=data))
