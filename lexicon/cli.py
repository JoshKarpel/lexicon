import sys
import random

import click
from click_didyoumean import DYMGroup

from halo import Halo
from spinners import Spinners

import lexicon
from .clifmt import print_words

SPINNERS = [name for name in Spinners.__members__ if 'dots' in name]
COLORS = ['red', 'blue', 'cyan', 'magenta', 'yellow', 'red']


def spinner(*args, **kwargs):
    return Halo(
        *args,
        spinner = random.choice(SPINNERS),
        color = random.choice(COLORS),
        stream = sys.stderr,
        **kwargs,
    )


CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

LIMIT_HELP = 'The maximum number of words returned.'


@click.group(context_settings = CONTEXT_SETTINGS, cls = DYMGroup)
def cli():
    """Lexicon command line tool."""
    pass


@cli.command()
@click.argument('word')
def define(word):
    """Find the definition of the given word."""
    with spinner():
        words = lexicon.define(
            word,
        )
    print_words(words)


@cli.command()
@click.argument('description')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def describe(description, limit):
    """Find words that match the given description."""
    with spinner():
        words = lexicon.describe(
            description,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def homophones(word, limit):
    """Find words that sound like the given word."""
    with spinner():
        words = lexicon.homophones(
            word,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def synonyms(word, limit):
    """Find words that are synonymous with the given word."""
    with spinner():
        words = lexicon.synonyms(
            word,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def antonyms(word, limit):
    """Find words that are antonymous with the given word."""
    with spinner():
        words = lexicon.antonyms(
            word,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--exact/--approximate',
    default = True,
    help = 'Find exact or approximate rhymes (default: exact).',
)
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def rhymes(word, exact, limit):
    """Find words that rhyme with the given word."""
    with spinner():
        words = lexicon.rhymes(
            word,
            exact = exact,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def supers(word, limit):
    """Find words that are a superset of the given word."""
    with spinner():
        words = lexicon.supers(
            word,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def subs(word, limit):
    """Find words that are subsets of the given word."""
    with spinner():
        words = lexicon.subs(
            word,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def parts(word, limit):
    """Find words that are parts of the given word."""
    with spinner():
        words = lexicon.parts(
            word,
            limit = limit,
        )
    print_words(words)


@cli.command()
@click.argument('word')
@click.option(
    '--limit',
    type = int,
    default = 10,
    help = LIMIT_HELP,
)
def partof(word, limit):
    """Find words that the given word is part of."""
    with spinner():
        words = lexicon.part_of(
            word,
            limit = limit,
        )
    print_words(words)
