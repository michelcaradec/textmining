#!/usr/bin/python
# -*- coding: utf-8 -*-


from setuptools import setup


setup(name="textmining",
      version="0.2",
      description="Tiny text mining package",
      url="https://github.com/michelcaradec/textmining",
      author="Michel Caradec",
      author_email="mcaradec@hotmail.com",
      license="MIT",
      packages=["textmining"],
      install_requires=[
          "unidecode",
      ],
      include_package_data=True,
      zip_safe=False)
