#!/usr/bin/python
# -*- coding: utf-8 -*-


class Singleton(object):
    """
    Singleton class.
    https://wiki.python.org/moin/SingletonProgramming
    """
    __singleton = None

    def get_singleton(cls):
        """
        Get class singleton.
        """
        if not isinstance(cls.__singleton, cls):
            cls.__singleton = cls()

        return cls.__singleton


    get_singleton = classmethod(get_singleton)
