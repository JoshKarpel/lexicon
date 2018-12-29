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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))


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
    click.echo('\n'.join(w.fmt() for w in words))
