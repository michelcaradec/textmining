#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import codecs
from singleton import Singleton
import tm
from firstnameinfo import FirstNameInfo


class FirstName(Singleton):
    """
    First name manipulation class.
    """

    count_threshold = 0
    """First name count threshold"""
    year_threshold = 0
    """First name year threshold"""
    confidence_threshold = 0
    """First name confidence threshold"""


    def __init__(self):
        self.__firstnames = None
        self.__exclusion = set()
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


    def reset_thresholds(self):
        """
        reset all thresholds.
        """
        self.count_threshold = 0
        self.year_threshold = 0
        self.confidence_threshold = 0


    def set_exclusion_list(self, firstnames, clean_token=True):
        """
        Set first names exclusion list (ie first names to ignore).
        """
        self.__exclusion = set(
            (self.__clean_firstname(token) if clean_token else token for token in firstnames)
        ) if firstnames else set()


    def get_exclusion_list(self):
        """
        Get first names exclusion list (ie first names to ignore).
        """
        return self.__exclusion if self.__exclusion else set()


    def get_info(self, token, clean_token=True):
        """
        Get first name infos.
        """
        self.__ensure_loaded()

        token = self.__clean_firstname(token) if clean_token else token
        info = self.__firstnames.get(token) if token not in self.__exclusion else None

        return info \
            if info \
                and info.count >= self.count_threshold \
                and info.confidence >= self.confidence_threshold \
                and info.year >= self.year_threshold \
            else None


    def is_firstname(self, token, clean_token=True):
        """
        Check if first name.
        """
        info = self.get_info(token, clean_token)

        return True if info else False


    def get_gender(self, token, clean_token=True):
        """
        Get first name gender:
        GENDER_MALE = male
        GENDER_FEMALE = female
        GENDER_BOTH = used for both
        None = Not a first name
        """
        info = self.get_info(token, clean_token)

        return info.gender if info else None


    def get_gender_confidence(self, token, clean_token=True):
        """
        Get first name gender and confidence:
        GENDER_MALE = male
        GENDER_FEMALE = female
        GENDER_BOTH = used for both
        None = Not a first name
        """
        info = self.get_info(token, clean_token)

        return (info.gender, info.confidence) if info else (None, None)
