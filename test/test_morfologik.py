# coding=utf-8

import unittest

from pymorfologik import Morfologik


class MorfologikTest(unittest.TestCase):
    def test_get_simple_stem(self):
        m = Morfologik()

        stemms = m.get_simple_stem(['tańczyłem', 'gra'])
        self.assertEquals(2, len(stemms))
        self.assertListEqual(['tańczyć'], stemms['tańczyłem'])
        self.assertEquals(['gra', 'grać'], stemms['gra'])

    def test_get_simple_stem_duplicates(self):
        m = Morfologik()

        stemms = m.get_simple_stem(['gra', 'gra', 'gra'])
        self.assertEquals(1, len(stemms))

    def test_get_simple_stem_word_does_not_exist(self):
        m = Morfologik()

        stemms = m.get_simple_stem(['niematakiegosłowa'])
        self.assertEquals(0, len(stemms))
