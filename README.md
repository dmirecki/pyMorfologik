# Python binding for Morfologik

Morfologik is Polish morphological analyzer. For more information see http://github.com/morfologik/morfologik-stemming/ and http://http://www.morfologik.blogspot.com/

## Requirements

This binding works with Python 2 and Python 3.

## Installation

For now, just colone the repo

 > git clone https://github.com/adibo/pyMorfologik.git

## Usage

Now, only simple stems are supported:

    >>> from pymorfologik import Morfologik
    >>> Morfologik().get_simple_stem(['Ala ma kota'])
    [('Ala', ['Ala', 'Al', 'Alo']),
     ('kota', ['kota', 'kot', 'kot', 'kot']),
     ('ma', ['mieć', 'mój'])]

### Acknowledgements

This repo is based on Morfologik, a great contribution of Marcin Miłowski (http://marcinmilkowski.pl) and Dawid Weiss (http://www.dawidweiss.com).
This repo is a fork and follow up of https://github.com/dmirecki/pyMorfologik.git