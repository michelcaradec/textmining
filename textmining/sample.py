#!/usr/bin/python
# -*- coding: utf-8 -*-


import tm
from stopwords import StopWords
from firstname import FirstName


def tm_demo():
    """
    Transformations demonstration.
    """
    transformations = [
        tm.clean, \
        tm.min_len(1), \
        tm.to_lower, \
        tm.remove_stopwords, \
        tm.substitute_accents]

    text = u"Les chaussettes de l'archiduchesse sont-elles sèches, archi-sèches ?"
    tokens = tm.tokenize_transform(text, transformations, lazy=False)

    print " ".join(tokens)
    print " ".join(sorted(set(tokens)))


def firstname_demo():
    """
    First name detection demonstration.
    """
    for firstname in [u"Mathilde", u"Gaëlle", u"Grégory", u"Rennes", u"Yann"]:
        print "%s is %sa first name." % (firstname, "" if tm.is_firstname(firstname) else "not ")

    # Check singleton: first names will only be loaded once.
    instance = FirstName.get_singleton()
    print instance.is_firstname(u"Michel")
    print instance.get_gender(u"Yann")


def tokenize_firstname_demo():
    """
    Tokenization and first name detection demonstration.
    """
    text = u"Bonjour, je m'appelle Abby-Gaëlle, j'habite Rennes."
    firstnames = tm.tokenize_transform(text, [tm.is_firstname], split_on_dash=False)
    for firstname in firstnames:
        print firstname


def main():
    """
    Main.
    """
    tm_demo()
    firstname_demo()
    tokenize_firstname_demo()


if __name__ == "__main__":
    main()
