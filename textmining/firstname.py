#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import codecs
from singleton import Singleton
import tm


class FirstName(Singleton):
    """
    First name manipulation class.
    """
    def __init__(self):
        self.__firstnames = None
        self.__filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/firstnames.txt")
        self.__encoding = "utf-8"


    def __load(self):
        """
        Load first names dictionary.
        """
        firstnames = dict()
        with codecs.open(self.__filename, "r", self.__encoding) as stream:
            for line in stream:
                prenom, gender = line.split()
                firstnames[prenom] = int(gender)
        return firstnames


    def __ensure_loaded(self):
        """
        Load first names dictionary if necessary.
        """
        if self.__firstnames is None:
            self.__firstnames = self.__load()


    def __clean_firstname(self, token):
        """
        First name cleaning.
        Remove accents, convert to lower case.
        """
        return tm.to_lower(tm.substitute_accents(token))


    def is_firstname(self, token, clean_token=True):
        """
        Check if first name.
        """
        self.__ensure_loaded()

        token = self.__clean_firstname(token) if clean_token else token
        return token in self.__firstnames


    def get_gender(self, token, clean_token=True):
        """
        Get first name gender:
        1 = male
        2 = female
        3 = used for both
        None = Not a first name
        """
        self.__ensure_loaded()

        token = self.__clean_firstname(token) if clean_token else token
        return self.__firstnames.get(token)
