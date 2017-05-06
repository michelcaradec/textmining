#!/usr/bin/python
# -*- coding: utf-8 -*-


from unidecode import unidecode


def to_lower(token):
    """
    Token to lower case.
    """
    return token.lower() if token else None


def substitute_accents(text):
    """
    Replace accents by corresponding ASCII characters.
    """
    return unidecode(text).encode("ascii")
