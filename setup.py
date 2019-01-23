import os
import re
from pathlib import Path

from setuptools import setup

THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def find_version():
    """Grab the version out of lexicon/__init__.py without importing it."""
    version_file_text = (Path(THIS_DIR) / 'lexicon' / '__init__.py').read_text()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file_text,
        re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name = 'lexicon',
    version = find_version(),
    author = 'Josh Karpel',
    author_email = 'josh.karpel@gmail.com',
    description = 'A command line tool for exploring words.',
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    url = 'https://github.com/JoshKarpel/lexicon',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    packages = [
        'lexicon',
    ],
    entry_points = {
        'console_scripts': [
            'lex = lexicon.cli:cli',
        ],
    },
    install_requires = Path('requirements.txt').read_text().splitlines(),
)
