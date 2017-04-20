#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import codecs
from singleton import Singleton
import tm


GENDER_MALE = 1
GENDER_FEMALE = 2
GENDER_BOTH = 3


class FirstNameInfo(object):
    """
    First name information class.
    """
    def __init__(self, m_year=0, m_count=0, f_year=0, f_count=0):
        self.m_year = m_year
        self.m_count = m_count
        self.f_year = f_year
        self.f_count = f_count
        self.__compute_gender()


    def __compute_gender(self):
        if self.m_count > self.f_count:
            self.gender = GENDER_MALE
            self.confidence = self.m_count / float(self.m_count + self.f_count)
        elif self.f_count > self.m_count:
            self.gender = GENDER_FEMALE
            self.confidence = self.f_count / float(self.m_count + self.f_count)
        else:
            self.gender = GENDER_BOTH
            self.confidence = .5


class FirstName(Singleton):
    """
    First name manipulation class.
    """
    def __init__(self):
        self.__firstnames = None
        self.__filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/firstnames.txt")
        self.__encoding = "utf-8"


    def __load(self):
        """
        Load first names dictionary.
        """
        firstnames = dict()

        with codecs.open(self.__filename, "r", self.__encoding) as stream:
            stream.next() # Header

            for line in stream:
                firstname, m_year, m_count, f_year, f_count = line.split("\t")
                f_count = f_count.strip()

                firstnames[firstname] = FirstNameInfo(
                    int(m_year) if m_year else 0,
                    int(m_count) if m_count else 0,
                    int(f_year) if f_year else 0,
                    int(f_count) if f_count else 0)

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


    def __get_info(self, token, clean_token=True):
        self.__ensure_loaded()

        token = self.__clean_firstname(token) if clean_token else token
        return self.__firstnames.get(token)


    def is_firstname(self, token, clean_token=True):
        """
        Check if first name.
        """
        info = self.__get_info(token, clean_token)

        return True if info else False


    def get_gender(self, token, clean_token=True):
        """
        Get first name gender:
        GENDER_MALE = male
        GENDER_FEMALE = female
        GENDER_BOTH = used for both
        None = Not a first name
        """
        info = self.__get_info(token, clean_token)

        return info.gender if info else None


    def get_gender_confidence(self, token, clean_token=True):
        """
        Get first name gender and confidence:
        GENDER_MALE = male
        GENDER_FEMALE = female
        GENDER_BOTH = used for both
        None = Not a first name
        """
        info = self.__get_info(token, clean_token)

        return (info.gender, info.confidence) if info else (None, None)
