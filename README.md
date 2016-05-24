[![Requirements Status](https://requires.io/github/lancelote/codewars/requirements.svg?branch=master)](https://requires.io/github/lancelote/codewars/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/codewars.svg?branch=master)](https://travis-ci.org/lancelote/codewars)


# codewars

[Codewars](http://www.codewars.com/) Kata Python solutions

## Project Structure

- [python2](python2/) or [python3](python3/) language version
    - [src](src/) - kata solutions sorted by rank
    - [tests](tests/) - tests to kata solutions (`test_<solution-filename>.py`)
      also sorted by rank
- [utils](utils/) - simple scripts I wrote to handle the project routines

## Prerequisites

- [Old katas](src/python2/) use Python 2, [new katas](src/python3/) - Python 3
- Requirements: `pip install -r requirements.txt` (`virtualenv` strongly suggested)

## Tests

Change `python2` to `python3` if needed

### Unit and Doc Tests

```bash
python -m pytest --doctest-modules python2/
```

### Syntax Validation

```bash
python -m pylint python2/src/ python2/tests/
```

## Utils

- [Kata Sorter](utils/kata_sorter.py) - rearranges file-mess from `src/` and
  `tests/` by rank subfolders

### Kata Sorter

Initially I did not sort solution and test files by ranks, so after a while
I got a file-mess in both `src/` and `tests/` directories. Because of big file
number I wrote a simple utility to auto-rearrange files between rank subfolders.

I have a standard docstring at the beginning of each solution file, which
contains url of the kata. The url itself holds slug or id of the kata.
With this in mind we can easily connect to [Codewars API](http://dev.codewars.com/)
and ask it about kata rank.

I used an old but good method to store sensitive information
([API key](http://dev.codewars.com/#authentication) in our case) - via
environment variables. Specifically - `ACCESS_KEY`. So set it up before
running the script or an error will occur.

To send HTTP requests to [Codewars API](http://dev.codewars.com/) I used
`concurrent.futures` for better performance.

## Contacts

Feel free to contact me if you have any questions or problems with this
repository, I would love to help!
