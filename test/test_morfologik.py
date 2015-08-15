# coding=utf-8

import unittest

from pymorfologik import Morfologik, DictParser


class MorfologikTest(unittest.TestCase):
    def test_get_simple_stem(self):
        stemms = Morfologik().stem(['tańczyłem', 'gra'], DictParser())
        self.assertEquals(2, len(stemms))
        self.assertListEqual(['tańczyć'], stemms['tańczyłem'])
        self.assertEquals(['gra', 'grać'], stemms['gra'])

    def test_get_simple_stem_duplicates(self):
        stemms = Morfologik().stem(['gra', 'gra', 'gra'], DictParser())
        self.assertEquals(1, len(stemms))

    def test_get_simple_stem_word_does_not_exist(self):
        stemms = Morfologik().stem(['niematakiegosłowa'], DictParser())
        self.assertEquals(0, len(stemms))
