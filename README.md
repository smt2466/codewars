[![Requirements Status](https://requires.io/github/lancelote/codewars/requirements.svg?branch=master)](https://requires.io/github/lancelote/codewars/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/codewars.svg?branch=master)](https://travis-ci.org/lancelote/codewars)


# codewars

[Codewars](http://www.codewars.com/) Kata Python solutions

## Prerequisites

Python 2+ only (Python 3 is not supported by codewars right now)

Requirements:
```bash
pip install -r requirements.txt
```

## Tests

### Unit and Doc Tests

```bash
python -m pytest --doctest-modules
```

### Syntax Validation

```bash
python -m pylint src tests
```
