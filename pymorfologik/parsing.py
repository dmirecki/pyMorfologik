# coding=utf-8
import abc
from collections import OrderedDict, defaultdict


class BaseParser(object):
    """Base parser for the morfologik output"""
    @abc.abstractmethod
    def parse(self, output, **kwargs):
        """Parse output of the morfologik"""
        return
    parse.__annotations__ = {'output': str}

    def _get_lines_with_stems(self, output, start=4, finish=-2):
        """
        Removes first four lines (morfologik run params description) as well as
        the last line (performance information).
        """
        return output.split('\n')[start:finish]
    _get_lines_with_stems.__annotations__ = {'output': str, 'return': list}


class DictParser(BaseParser):
    """
    DictParser parses the morfologik output string to produce a dict with
    stems for output words. Each output word appears only once in the resulting
    dict.
    """
    def _make_unique(self, words):
        keys = OrderedDict()
        for e in words:
            keys[e] = 1
        return keys.keys()

    def _parse_for_simple_stems(self, lines):
        stems = defaultdict(lambda: [])

        for line in lines:
            original_word, stem, _ = line.split("\t")

            if stem == '-':
                continue

            stems[original_word].append(stem)
        return dict(stems)

    def parse(self, output):
        """
        Find stems for a given text.
        """
        output = self._get_lines_with_stems(output)
        words = self._make_unique(output)
        return self._parse_for_simple_stems(words)
    parse.__annotations__ = {'output': list, 'return': dict}


class ListParser(BaseParser):
    """
    ListParser parses the morfologik output string to produce a list of tuples
    with stems for each output word. Each output word may appear several times
    in the resulting list.
    """
    def parse(self, output, skip_empty=False, skip_same=True):
        lines_with_stems = self._get_lines_with_stems(output)

        stems = list()
        last_word = None

        for line in lines_with_stems:
            word, stem, _ = line.split("\t")
            stem = stem if stem != '-' else None

            if skip_empty and (stem is None):
                continue

            if last_word != word:
                stems.append((word, []))

            ## append new stem only if not on list already
            stem = None if skip_same and stem in stems[-1][1] else stem
            if stem is not None:
                stems[-1][1].append(stem)

            last_word = word

        return stems
    parse.__annotations__ = {'output': str,
                             'skip_empty': bool, 'skip_same': bool,
                             'return': list}
