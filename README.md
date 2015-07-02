# Python binding for Morfologik

Morfologik is Polish morphological analyzer. For more information see http://github.com/morfologik/morfologik-stemming/ and http://http://www.morfologik.blogspot.com/

## Requirements

This binding works only with Python 3.

## Installation

Install it from pip:

`> pip install pyMorfologik`

## Usage

Now, only simple stems are supported:

    >>> from pymorfologik import Morfologik
    >>> Morfologik().get_simple_stem(['tañczy³em', 'gra'])
    {'gra': ['gra', 'graæ'], 'tañczy³em': ['tañczyæ']}

