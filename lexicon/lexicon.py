from typing import List

from dataclasses import dataclass

import requests

API_URL = r'https://api.datamuse.com/words?'


@dataclass(frozen = True)
class Word:
    word: str
    definitions: list

    def __str__(self):
        return self.word

    def __len__(self):
        return len(self.word)


@dataclass(frozen = True)
class Definition:
    part: str
    text: str

    def __str__(self):
        return f'[{self.part.center(3)}] {self.text}'

    def __len__(self):
        return len(str(self))


def _get_words(params, limit = None):
    params = {**params, 'md': 'dp', 'max': limit}
    j = requests.get(API_URL, params = params).json()

    words = []
    for entry in j:
        defs = [Definition(*definition.split('\t')) for definition in entry.get('defs', [])]

        w = Word(
            entry['word'],
            defs,
        )
        words.append(w)

    return words


def define(word) -> List[Word]:
    params = {
        'sp': word,
    }
    return _get_words(params, limit = 1)


def describe(description, limit = None) -> List[Word]:
    params = {
        'ml': '+'.join(description.split()),
    }
    return _get_words(params, limit = limit)


def homophones(word, limit = None) -> List[Word]:
    params = {
        'sl': word,
    }
    return _get_words(params, limit = limit)


def synonyms(word, limit = None) -> List[Word]:
    params = {
        'rel_syn': word,
    }
    return _get_words(params, limit = limit)


def antonyms(word, limit = None) -> List[Word]:
    params = {
        'rel_ant': word,
    }
    return _get_words(params, limit = limit)


def rhymes(word, exact = True, limit = None) -> List[Word]:
    params = {
        'rel_rhy' if exact else 'rel_nry': word,
    }
    return _get_words(params, limit = limit)


def supers(word, limit = None) -> List[Word]:
    params = {
        'rel_spc': word,
    }
    return _get_words(params, limit = limit)


def subs(word, limit = None) -> List[Word]:
    params = {
        'rel_gen': word,
    }
    return _get_words(params, limit = limit)


def parts(word, limit = None) -> List[Word]:
    params = {
        'rel_com': word,
    }
    return _get_words(params, limit = limit)


def part_of(word, limit = None) -> List[Word]:
    params = {
        'rel_par': word,
    }
    return _get_words(params, limit = limit)
