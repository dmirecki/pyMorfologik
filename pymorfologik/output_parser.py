# coding=utf-8


def _stem_found(stem):
    return stem != '-'
_stem_found.__annotations__ = {'stem': str, 'return': bool}


def _get_lines_with_stems(morfologik_output):
    """
    Removes first four lines (morfologik run params description) as well as
    the last line (performance information).
    """
    return morfologik_output.split("\n")[4:-2]
_get_lines_with_stems.__annotations__ = {'morfologik_output': str,
                                         'return': list}


def parse_for_simple_stems(input, skip_empty=False):
    """
    Parses the output stem lines to produce a list with possible stems
    for each word in the input.

    :param skip_empty: set True to skip lines without stems (default is False)
    :returns: a list of tuples, each containing an original text word and
              a list of stems for the given word
    """
    lines_with_stems = _get_lines_with_stems(input)
    stems = list()

    last_word = None
    for line in lines_with_stems:
        word, stem, _ = line.split("\t")

        if skip_empty and not _stem_found(stem):
            continue

        if last_word != word:
            stems.append((word, []))

        stems[-1][1].append(stem)
        last_word = word

    return stems
parse_for_simple_stems.__annotations__ = {'output': str, 'return': dict}