[![Requirements Status](https://requires.io/github/lancelote/codewars/requirements.svg?branch=master)](https://requires.io/github/lancelote/codewars/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/codewars.svg?branch=master)](https://travis-ci.org/lancelote/codewars)


# codewars

[Codewars](http://www.codewars.com/) Kata Python solutions

## Project Structure

- [src](src/) - kata solutions sorted by rank
- [tests](tests/) - tests to kata solutions (`test_<solution-filename>.py`)
  also sorted by rank
- [utils](utils/) - simple scripts I wrote to handle the project routines

## Prerequisites

- Python 2+ only (Python 3 is not supported by codewars right now)
- Requirements: `pip install -r requirements.txt` (`virtualenv` strongly suggested)

## Tests

### Unit and Doc Tests

```bash
python -m pytest --doctest-modules
```

### Syntax Validation

```bash
python -m pylint src/ tests/
```

## Utils

- [Kata Sorter](utils/kata_sorter.py) - rearrange file-mess from `src/` and
  `tests/` by rank sub folders, uses Codewars API and `concurrent.futures` for
  multiple request handling
