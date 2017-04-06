#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
from singleton import Singleton


class Tokenizer(Singleton):
    """
    Tokenization class.
    """
    def __init__(self):
        self.__re_dash = re.compile(u"[^a-zA-Zà-ÿ\-]")
        self.__re_no_dash = re.compile(u"[^a-zA-Zà-ÿ]")


    def tokenize(self, text, split_on_dash=True):
        """
        Extract tokens from text.
        """
        return (self.__re_no_dash.sub(" ", text) if split_on_dash \
            else self.__re_dash.sub(" ", text)).split()
