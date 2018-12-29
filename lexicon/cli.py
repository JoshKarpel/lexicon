from typing import List

import sys
import random

import click
from click_didyoumean import DYMGroup

from halo import Halo
from spinners import Spinners

import lexicon

SPINNERS = list(name for name in Spinners.__members__ if 'dots' in name)


def make_spinner(*args, **kwargs):
    return Halo(
        *args,
        spinner = random.choice(SPINNERS),
        stream = sys.stderr,
        **kwargs,
    )


CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])


@click.group(context_settings = CONTEXT_SETTINGS, cls = DYMGroup)
def cli():
    """Lexicon command line tool."""
    pass


@cli.command()
@click.argument(
    'word',
)
def define(word):
    """Find the definition of the given word."""
    with make_spinner():
        words = lexicon.define(
            word,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'description',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def describe(description, limit):
    """Find words that match the given description."""
    with make_spinner():
        words = lexicon.describe(
            description,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def homophones(word, limit):
    """Find words that sound like the given word."""
    with make_spinner():
        words = lexicon.homophones(
            word,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def synonyms(word, limit):
    """Find words that are synonymous with the given word."""
    with make_spinner():
        words = lexicon.synonyms(
            word,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def antonyms(word, limit):
    """Find words that are antonymous with the given word."""
    with make_spinner():
        words = lexicon.antonyms(
            word,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def rhymes(word, limit):
    """Find words that (approximately) rhyme with the given word."""
    with make_spinner():
        words = lexicon.rhymes(
            word,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def supers(word, limit):
    """Find words that are a superset of the given word."""
    with make_spinner():
        words = lexicon.supers(
            word,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def subs(word, limit):
    """Find words that are subsets of the given word."""
    with make_spinner():
        words = lexicon.subs(
            word,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def parts(word, limit):
    """Find words that are parts of the given word."""
    with make_spinner():
        words = lexicon.parts(
            word,
            limit = limit,
        )
    _print_words(words)


@cli.command()
@click.argument(
    'word',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
)
def partof(word, limit):
    """Find words that the given word is part of."""
    with make_spinner():
        words = lexicon.partof(
            word,
            limit = limit,
        )
    _print_words(words)


PART_TO_COLOR = {
    'n': 'green',
    'v': 'cyan',
    'adj': 'red',
    'adv': 'yellow',
}


def _fmt_word(word: lexicon.Word, longest_word_len = None) -> str:
    if longest_word_len is None:
        longest_word_len = len(word)

    parts = [f'{word} {"-" * (longest_word_len - len(word) + 1)}>']
    prefix = ' ' * len(parts[0])

    if len(word.definitions) == 0:
        parts.append('NO DEFINITIONS FOUND\n')

    parts.extend(
        click.style(
            f'{prefix if idx != 0 else ""} {definition}\n',
            fg = PART_TO_COLOR[definition.part],
        )
        for idx, definition in enumerate(word.definitions)
    )

    return ''.join(parts)


def _fmt_words(words: List[lexicon.Word]) -> str:
    longest_word_len = max(len(w) for w in words)
    return '\n'.join(_fmt_word(w, longest_word_len) for w in words)


def _print_words(words: List[lexicon.Word]):
    click.echo(_fmt_words(words))
