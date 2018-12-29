import math
from typing import List

import click

import lexicon


def _brace(index, num_definitions):
    if num_definitions == 1:
        return '<'
    elif index == 0:
        return '/'
    elif index == num_definitions - 1:
        return '\\'
    else:
        return '|'


PART_TO_COLOR = {
    'n': 'green',
    'v': 'cyan',
    'adj': 'red',
    'adv': 'yellow',
    'u': 'magenta',
}


def _line_char(num_definitions):
    if num_definitions == 2:
        return '_'

    return '-'


def _fmt_word(word: lexicon.Word, longest_word_len = None) -> str:
    if longest_word_len is None:
        longest_word_len = len(word)

    len_line = longest_word_len - len(word) + 1
    num_definitions = len(word.definitions)

    start = f'{click.style(str(word), bold = True)} {_line_char(num_definitions) * len_line}'
    if num_definitions == 0:
        return f'{start}< {click.style("NO DEFINITIONS FOUND", fg = "magenta")}'

    center = math.floor((num_definitions - 1) / 2)
    prefix = ' ' * (len(word) + len_line + 1)
    parts = []
    for idx, definition in enumerate(word.definitions):
        p = prefix if idx != center else start
        b = _brace(idx, num_definitions)
        d = click.style(str(definition), fg = PART_TO_COLOR[definition.part])
        parts.append(f'{p}{b} {d}')

    return '\n'.join(parts)


def _fmt_words(words: List[lexicon.Word]) -> str:
    if len(words) == 0:
        return 'NO WORDS FOUND'

    longest_word_len = max(len(w) for w in words)
    return '\n\n'.join(_fmt_word(w, longest_word_len) for w in words)


def print_words(words: List[lexicon.Word]):
    click.echo(_fmt_words(words))
