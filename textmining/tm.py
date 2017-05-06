#!/usr/bin/python
# -*- coding: utf-8 -*-


import utils
from stopwords import StopWords
from firstname import FirstName
from tokenizer import Tokenizer


def remove_stopwords(token):
    """
    Remove stop words using default StopWords instance.
    """
    return StopWords.get_singleton().remove(token)


def remove_stopwords_inst(sw_instance):
    """
    Remove stop words using provided StopWords instance.
    """
    return sw_instance.remove


def clean(token):
    """
    Remove blank characters.
    """
    return token.strip() if token else None


def to_lower(token):
    """
    Token to lower case.
    """
    return utils.to_lower(token)


def min_len(length):
    """
    Minimum length filter function.
    """
    return lambda token: None if len(token) < length else token


def is_firstname(token):
    """
    First name filter function.
    """
    return token if FirstName.get_singleton().is_firstname(token) else None


def is_gender(gender, clean_token=True):
    """
    First name gender filter function.
    1 = male
    2 = female
    3 = used for both
    """
    return lambda token: \
        token \
        if FirstName.get_singleton().get_gender(token, clean_token) == gender \
        else None


def substitute_accents(text):
    """
    Replace accents by corresponding ASCII characters.
    """
    return utils.substitute_accents(text)


def tokenize(text, split_on_dash=True):
    """
    Extract tokens from text.
    """
    return Tokenizer.get_singleton().tokenize(text, split_on_dash)


def transform(token, operations=None):
    """
    Apply transformations to token.
    """
    for operation in operations if operations else []:
        token = operation(token)
        if token is None:
            break

    return token


def tokenize_transform(text, operations=None, lazy=True, split_on_dash=True):
    """
    Extract and transform tokens from text.
    """
    tokens = (
        token \
        for token \
        in (transform(token, operations) for token in tokenize(text, split_on_dash)) \
        if token)
    if lazy:
        # Return generator
        return tokens
    else:
        return list(tokens)
