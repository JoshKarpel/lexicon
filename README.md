# Lexicon

Lexicon uses the [Datamuse API](https://www.datamuse.com/api/) to explore the wonderful world of words.
It provides a wide variety of simple CLI commands to look for words that have some relationship to a word or description that you provide.

## Installation

Install by running

```bash
pip install git+https://github.com/JoshKarpel/lexicon.git
```

and then use Lexicon from the command line by running `lex`.

Lexicon requires `Python >3.7`.

## Examples

Get the definition of a word:

```
$ lex define quickly
         / [adv] with rapid movements
quickly -| [adv] with little or no delay
         \ [adv] without taking pains
```

Get synonyms for a word:

```
$ lex synonyms write
             / [ n ] a verbal formula believed to have magical force
             | [ n ] a psychological state induced by (or as if induced by) a magical incantation
             | [ n ] a time for working (after which you will be relieved by someone else)
spell -------| [ n ] a period of indeterminate length (usually short) marked by some action or condition
             | [ v ] indicate or signify
             | [ v ] recite the letters of or give the spelling of
             | [ v ] place under a spell
             \ [ v ] write or name the letters that comprise the conventionally accepted form of (a word or part of a word)

             / [ n ] female swan
             | [ n ] a writing implement with a point from which ink flows
pen ---------| [ n ] an enclosure for confining livestock
             | [ n ] a correctional institution for those convicted of major crimes
             \ [ n ] a portable enclosure in which babies may be left to play

             / [ v ] form the substance of
             | [ v ] put together out of existing material
compose -----| [ v ] write music
             | [ v ] calm (someone, especially oneself); make quiet
             | [ v ] draw up the plans or basic details for
             \ [ v ] produce a literary work

             / [ v ] prepare and issue for public distribution or sale
publish -----| [ v ] have (one's written work) issued for publication
             \ [ v ] put into print

indite ------< [ v ] produce a literary work

drop a line -< [ v ] communicate (with) in writing
```

Get words that this word is "part of":

```
$ lex partof bark
            / [ n ] the part of a tooth that is embedded in the jaw and serves as support
            | [ n ] (linguistics) the form of a word after all affixes are removed
            | [ n ] (botany) the usually underground organ that lacks buds or leaves or nodes; absorbs water and mineral salts; usually it anchors the plant to the ground
root -------| [ n ] a number that when multiplied by itself some number of times equals a given number
            | [ n ] a simple form inferred as the common basis from which related words in several languages can be derived by linguistic processes
            | [ n ] the set of values that give a true statement when substituted into an equation
            | [ n ] the place where something begins, where it springs into being
            \ [ n ] someone from whom you are descended (but usually more remote than a grandparent)

            / [ n ] an administrative division of some larger or more complex organization
            | [ n ] a stream or river connected to a larger one
branch -----| [ n ] a division of a stem, or secondary stem arising from the main stem of a plant
            | [ n ] a part of a forked or branching shape
            | [ n ] any projection that is thought to resemble an arm
            \ [ n ] a natural consequence of development

            / [ n ] luggage consisting of a large strong case used when traveling or for storage
            | [ n ] the main stem of a tree; usually covered with bark; the bole is usually the part that is commercially useful for lumber
trunk ------| [ n ] a long flexible snout as of an elephant
            | [ n ] the body excluding the head and neck and limbs
            \ [ n ] compartment in an automobile that carries luggage or shopping or tools

            / [ n ] a Chadic language spoken in northern Nigeria and closely related to Hausa
bole -------| [ n ] a soft oily clay used as a pigment (especially a reddish brown pigment)
            \ [ n ] the main stem of a tree; usually covered with bark; the bole is usually the part that is commercially useful for lumber

tree trunk -< [ n ] the main stem of a tree; usually covered with bark; the bole is usually the part that is commercially useful for lumber
```
