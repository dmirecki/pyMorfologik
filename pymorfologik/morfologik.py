# coding=utf-8

import os
import subprocess

from pyMorfologik.output_parser import parse_for_simple_stems


class Morfologik(object):
    def __init__(self, jar_path=''):
        self.jar_path = jar_path

        if self.jar_path == '':
            this_dir, _ = os.path.split(__file__)
            self.jar_path = os.path.join(this_dir, "jar/morfologik1.9.jar")
    __init__.__annotations__ = {'jar_path': str}

    def get_simple_stem(self, words):
        """
        Find stems for a given text.

        Example:
        Morfologik().get_simple_stem(['ja tańczę a ona śpi'])
        returns
        {
             'ja': ['ja'],
             'tańczę': ['tańczyć'],
             'a': ['a'],
             'ona': ['on'],
             'śpi': ['spać']
        }

        Notes: captions and interpunction may not always work.
        """
        words = self._make_unique(words)
        output = self._run_morfologik(words)
        return parse_for_simple_stems(output)
    get_simple_stem.__annotations__ = {'words': list, 'return': dict}

    def _run_morfologik(self, words):
        """
        Runs morfologik java jar and assumes that input and output is
        UTF-8 encoded.
        """
        p = subprocess.Popen(
            ['java', '-jar', self.jar_path, 'plstem',
             '-ie', 'UTF-8',
             '-oe', 'UTF-8'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        out, _ = p.communicate(input=bytes("\n".join(words), "UTF-8"))
        return out.decode()
    _run_morfologik.__annotations__ = {'words': list, 'return': str}

    def _make_unique(self, words):
        keys = {}
        for e in words:
            keys[e] = 1
        return keys.keys()
