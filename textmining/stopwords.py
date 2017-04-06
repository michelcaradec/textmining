#!/usr/bin/python
# -*- coding: utf-8 -*-


import codecs
from singleton import Singleton
import tm


class StopWords(Singleton):
    """
    StopWords class.
    """
    def __init__(self):
        self.__filename = "assets/stopwords_french.txt"
        self.__encoding = "utf-8"
        self.__stopwords = None


    def __load(self):
        """
        Load stop words dictionary.
        """
        stopwords = set()
        with codecs.open(self.__filename, "r", self.__encoding) as stream:
            for word in stream:
                stopwords.add(word.strip().lower())

        return stopwords


    def init(self, filename, encoding=None, load=True):
        """
        Initialize class with a stopwords file.
        """
        self.__filename = filename
        self.__encoding = encoding

        if load:
            self.__load()

        return self


    def remove(self, token):
        """
        Remove stop words.
        """
        if self.__stopwords is None:
            self.__stopwords = self.__load()

        return None if tm.to_lower(tm.substitute_accents(token)) in self.__stopwords else token
