[![Requirements Status](https://requires.io/github/lancelote/codewars/requirements.svg?branch=master)](https://requires.io/github/lancelote/codewars/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/codewars.svg?branch=master)](https://travis-ci.org/lancelote/codewars)


# codewars

[Codewars](http://www.codewars.com/) Kata Python solutions

## Project Structure

- [python2](python2/) - Python 2 katas
- [python3](python3/) - Python 3 katas
- [tests](tests/) - tests for both language version katas and utils
- [utils](utils/) - simple scripts I wrote to handle the project routines

## Prerequisites

- [Old katas](python2/) use Python 2, [new katas](python3/) - Python 3
- Requirements: `pip install -r requirements.txt` (`virtualenv` strongly suggested)

### System Variables

I used an old but good method to store sensitive information
([API key](http://dev.codewars.com/#authentication) in our case) - via
environment variables. So set it up before running the utils scripts or an
error will occur. Solutions or kata tests do not rely on the system variables

| Variable | Note |
| :---: | :---: |
| ACCESS_KEY | Your unique Codewars [API key](http://dev.codewars.com/#authentication) |

## Tests

Change `python2` to `python3` if needed

### Unit and Doc Tests

```bash
python -m pytest --doctest-modules python2/ tests/python2/
```

### Syntax Validation

```bash
python -m pylint python2/ tests/python2/
```

## Utils

- [Kata Sorter](utils/kata_sorter.py) - rearranges file-mess from `src/` and
  `tests/` by rank subfolders
- [New Kata](utils/new_solution.py) - creates solution and test templates for
  a given kata (calls codewars API with a given slug)

### Kata Sorter

Initially I did not sort solution and test files by ranks, so after a while
I got a file-mess in both `src/` and `tests/` directories. Because of big file
number I wrote a simple utility to auto-rearrange files between rank subfolders.

I have a standard docstring at the beginning of each solution file, which
contains url of the kata. The url itself holds slug or id of the kata.
With this in mind we can easily connect to [Codewars API](http://dev.codewars.com/)
and ask it about kata rank.

To send HTTP requests to [Codewars API](http://dev.codewars.com/) I used
`concurrent.futures` for better performance.

### New Kata

`python manage.py new <kata-slug-or-id> python2` (or `python3`)

Calls to Codewars API with the given slug or id (can be extracted from the url),
retrieves kata data (rank, description, url) and creates solution and test
templates (based on [jinja2 templates](utils/templates/)) in the correct
directories

## Contacts

Feel free to contact me if you have any questions or problems with this
repository, I would love to help!
