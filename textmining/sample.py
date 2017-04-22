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

    # Singleton mechanism make first name asset is loaded once.
    instance = FirstName.get_singleton()
    print instance.is_firstname(u"Michel")

    # Exclusion list (used to exclude ambiguous first names)
    print instance.is_firstname(u"France")
    instance.set_exclusion_list([u"France"])
    print instance.get_exclusion_list()
    print instance.is_firstname(u"France")

    # Confidence threshold (used to exclude uncertain first names)
    print instance.get_gender_confidence(u"Yann")
    FirstName.get_singleton().confidence_threshold = 1
    print instance.is_firstname(u"Yann")

    # Count threshold (used to exclude rare first names)
    info = instance.get_info(u"Framboise")
    print info.count
    FirstName.get_singleton().count_threshold = info.count + 1
    print instance.is_firstname(u"Framboise")

    # Year threshold (used to exclude old first names)
    info = instance.get_info(u"Leoncine")
    print info.year
    FirstName.get_singleton().count_threshold = info.year + 1
    print instance.is_firstname(u"Leoncine")

    instance.reset_thresholds()


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
