#!/usr/bin/python
# -*- coding: utf-8 -*-


GENDER_MALE = 1
GENDER_FEMALE = 2
GENDER_BOTH = 3


class FirstNameInfo(object):
    """
    First name information class.
    """

    gender = None
    """First name gender"""
    count = None
    """First name gender occurences"""
    year = None
    """Most recent year first name was given"""
    confidence = None
    """Gender estimation confidence"""


    def __init__(self, m_year=0, m_count=0, f_year=0, f_count=0):
        self.m_year = m_year
        self.m_count = m_count
        self.f_year = f_year
        self.f_count = f_count
        self.__compute_gender()


    def __compute_gender(self):
        """
        Estimate gender.
        """
        if self.m_count > self.f_count:
            self.count = self.m_count
            self.gender = GENDER_MALE
            self.year = self.m_year
            self.confidence = self.m_count / float(self.m_count + self.f_count)
        elif self.f_count > self.m_count:
            self.count = self.f_count
            self.gender = GENDER_FEMALE
            self.year = self.f_year
            self.confidence = self.f_count / float(self.m_count + self.f_count)
        else:
            self.count = self.m_count
            self.gender = GENDER_BOTH
            self.year = self.m_year
            self.confidence = .5
