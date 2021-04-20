#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requires = f.read().splitlines()

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-ordered-model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="3.4.2",
    description="Allows Django models to be ordered and provides a simple admin interface for reordering them.",
    author="Ben Firshman",
    author_email="ben@firshman.co.uk",
    url="http://github.com/django-ordered-model/django-ordered-model",
    packages=find_packages(),
    requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
    package_data={
        "ordered_model": [
            "static/ordered_model/arrow-up.gif",
            "static/ordered_model/arrow-down.gif",
            "static/ordered_model/arrow-top.gif",
            "static/ordered_model/arrow-bottom.gif",
            "locale/de/LC_MESSAGES/django.po",
            "locale/de/LC_MESSAGES/django.mo",
            "locale/pl/LC_MESSAGES/django.po",
            "locale/pl/LC_MESSAGES/django.mo",
            "templates/ordered_model/admin/order_controls.html",
        ]
    },
)
