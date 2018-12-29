__version__ = "0.1.0"

from .lexicon import (
    Word,
    Definition,
    define,
    describe,
    homophones,
    synonyms,
    antonyms,
    rhymes,
    supers,
    subs,
    parts,
    part_of,
)


def version() -> str:
    """Return a string containing human-readable version information."""
    return f'Lexicon version {__version__}'


def _version_info(v: str) -> tuple:
    """Un-format ``__version__``."""
    return (*(int(x) for x in v[:5].split('.')), v[5:])


def version_info() -> tuple:
    """Return a tuple of version information: ``(major, minor, micro, release_level)``."""
    return _version_info(__version__)
