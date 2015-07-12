# coding=utf-8

import os
import subprocess

from pyMorfologik.output_parser import parse_for_simple_stemms


class Morfologik(object):
    def __init__(self, jar_path: str=''):
        self.jar_path = jar_path

        if self.jar_path == '':
            this_dir, _ = os.path.split(__file__)
            self.jar_path = os.path.join(this_dir, "jar/morfologik1.9.jar")

    def get_simple_stem(self, words: list) -> dict:
        """
        Find only stemms for given words.

        For example:
        When given words ['gra', 'tańczyłem'] it returns
        {
            'gra': ['gra', 'grać'],
            'tańczyłem': ['tańczyć']
        }
        """
        words = self._make_unique(words)
        output = self._run_morfologik(words)
        return parse_for_simple_stemms(output)

    def _run_morfologik(self, words: list) -> str:
        """
        Run morfologik and assumes that input and output is UTF-8 encoded.
        """
        p = subprocess.Popen(['java', '-jar', self.jar_path, 'plstem', '-ie', 'UTF-8', '-oe', 'UTF-8'],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        out, _ = p.communicate(input=bytes("\n".join(words), "UTF-8"))

        return out.decode()

    def _make_unique(self, words):
        keys = {}
        for e in words:
            keys[e] = 1
        return keys.keys()
