# Python binding for Morfologik

Morfologik is Polish morphological analyzer. For more information see http://github.com/morfologik/morfologik-stemming/ and http://http://www.morfologik.blogspot.com/

## Requirements

This binding works with Python 2 and Python 3.

## Installation

Install it from pip
 > pip install pyMorfologik

or directly from github
 > git clone https://github.com/dmirecki/pyMorfologik.git

## Usage

Now, only simple stems are supported:

    >>> from pymorfologik import Morfologik
    >>> from pymorfologik.parsing import ListParser
    >>>
    >>> parser = ListParser()
    >>> stemmer = Morfologik()
    >>> stemmer.stem(['Ala ma kota'], parser)
    [(u'Ala',
      {u'Al': [u'subst:sg:acc:m1+subst:sg:gen:m1'],
       u'Ala': [u'subst:sg:nom:f'],
       u'Alo': [u'subst:sg:acc:m1+subst:sg:gen:m1']}),
     (u'ma',
      {u'mieć': [u'verb:fin:sg:ter:imperf:refl.nonrefl'],
       u'mój': [u'adj:sg:nom.voc:f:pos']}),
     (u'kota', {u'kot': [u'subst:sg:acc:m1'], u'kota': [u'subst:sg:nom:f']})]

### Acknowledgements

This repo is based on Morfologik, a great contribution of Marcin Miłowski (http://marcinmilkowski.pl) and Dawid Weiss (http://www.dawidweiss.com).


### Contributions
Damian Mirecki

Adrian Bohdanowicz