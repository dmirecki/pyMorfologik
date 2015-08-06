# coding=utf-8

from collections import defaultdict


def _stem_found(stem):
    return stem != '-'
_stem_found.__annotations__ = {'stem': str, 'return': bool}


def _get_lines_with_stemms(morfologik_output):
    """
    Removes first four lines (morfologik run params description) as well as
    the last line (performance information).
    """
    return morfologik_output.split("\n")[4:-2]
_get_lines_with_stemms.__annotations__ = {'morfologik_output': str,
                                         'return': list}


def parse_for_simple_stemms(output):
    lines_with_stems = _get_lines_with_stemms(output)

    stemms = defaultdict(lambda: [])

    for line in lines_with_stems:
        original_word, stem, _ = line.split("\t")

        if not _stem_found(stem):
            continue

        stemms[original_word].append(stem)

    return dict(stemms)
parse_for_simple_stemms.__annotations__ = {'output': str, 'return': dict}