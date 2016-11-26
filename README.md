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
- Requirements: `pip install -r requirements.txt` (virtual environment is
  strongly suggested)

### System Variables

Utilities and utility tests requires Codewars [API key](http://dev.codewars.com/#authentication).
Store it inside `utils/envs.py`:

```bash
touch utils/envs.py
echo "ACCESS_KEY='<your_api_key>'" > utils/envs.py
```

## Tests

I use `pytest` to run test suit. Unfortunately it's impossible to switch to
`nose` or `unittest` because `pytest` syntax is heavily used (fixtures,
parametrization and so on). Still you can freely write `unittest`-style tests if
needed - `pytest` understands it correctly. Flag `--doctest-modules` is also
used to analyze doctests (there're few here and there).

For syntax style validation `pylint` is used.

Language version will be auto selected according to active virtual environment.

### Unit and Doc Tests

```bash
invoke test
```

### Syntax Validation

```bash
invoke syntax
```

## Utils

### Active

- `invoke new <slug>` - creates new solution and test files depends on the given
  kata slug (uses `jinja2` and codewars API), for example: `invoke new
  hello-world` will be call codewars API to provide a description and
  difficulty level for the `hello-world` kata (you can check kata's slug in
  it's url). In case of success - `hello_world.py` and `test_hello_world.py`
  will be created in the corresponding folders (according to active Python
  version and kata difficulty level).

### Dated

- `invoke update` - updates dependencies of Python 2 and Python 3 pyenv virtual
  environments (`codewars2` and `codewars3`).
- `invoke sort` - was used to sort old kata files depends on the language
  version (uses codewars API and `concurrent.futures` for performance)

## Contacts

Feel free to contact me if you have any questions or problems with this
repository, I would love to help!
