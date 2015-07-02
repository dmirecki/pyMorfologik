# coding=utf-8

from collections import defaultdict


def _stem_found(stem: str) -> bool:
    return stem != '-'


def _get_lines_with_stemms(morfologik_output: str) -> list:
    """
    Removes first four lines (morfologik run params description) and last line (performance information).
    """
    return morfologik_output.split("\n")[4:-2]


def parse_for_simple_stemms(output: str) -> dict:
    lines_with_stemms = _get_lines_with_stemms(output)

    stemms = defaultdict(lambda: [])

    for line in lines_with_stemms:
        original_word, stem, _ = line.split("\t")

        if not _stem_found(stem):
            continue

        stemms[original_word].append(stem)

    return dict(stemms)
