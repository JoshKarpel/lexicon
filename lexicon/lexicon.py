from typing import List

from dataclasses import dataclass

import requests

API_URL = r'https://api.datamuse.com/words?'


@dataclass(frozen = True)
class Word:
    word: str
    definitions: list

    def fmt(self):
        s = f'{self.word} -> '
        prefix = ' ' * len(s)

        if len(self.definitions) == 0:
            s += 'NO DEFINITIONS FOUND\n'
            return s

        for idx, definition in enumerate(self.definitions):
            s += (prefix if idx != 0 else '') + definition.fmt() + '\n'

        return s


@dataclass(frozen = True)
class Definition:
    part: str
    text: str

    def fmt(self):
        return f'[{self.part}] {self.text}'


def _get_words(params, limit = None):
    params['md'] = 'dp'
    params['max'] = limit
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


def rhymes(word, limit = None) -> List[Word]:
    params = {
        'rel_nry': word,
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


def partof(word, limit = None) -> List[Word]:
    params = {
        'rel_par': word,
    }
    return _get_words(params, limit = limit)
