[![Maintainability](https://api.codeclimate.com/v1/badges/8868e0a8226c17bee3da/maintainability)](https://codeclimate.com/github/karomag/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8868e0a8226c17bee3da/test_coverage)](https://codeclimate.com/github/karomag/python-project-lvl2/test_coverage)
[![Build Status](https://travis-ci.com/karomag/python-project-lvl2.svg?branch=master)](https://travis-ci.com/karomag/python-project-lvl2)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![Build app](https://github.com/karomag/python-project-lvl2/workflows/Build%20app/badge.svg?branch=master&event=push)


# Project "Generate diff" (level 2)

## Description
CLI compares two configuration files and shows the differences.

```bash
$ gendiff -h

usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit

format settings:
  -f FORMAT, --format FORMAT
                        set format of output
```

## Installation

```bash
$ pip install --user --index-url https://test.pypi.org/simple/ karomag-gendiff --extra-index-url https://pypi.org/simple/
```

## Comparing two flat files.
before.yml
```yaml
  "host": "hexlet.io"
  "timeout": 50
  "proxy": "123.234.53.22"
  "language": "en"
```
after.yml
```yaml
  "timeout": 20
  "verbose": true
  "host": "hexlet.io"
  "language": "ru"
```

[![asciicast](https://asciinema.org/a/iRkttdJLEv8ahss3BYAGF2FZE.svg)](https://asciinema.org/a/iRkttdJLEv8ahss3BYAGF2FZE)

### The test data set of nested structures.
before.json
```json
{
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": true,
    "setting6": {
      "key": "value"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  }
}
```
after.json
```json
{
  "common": {
    "setting1": "Value 1",
    "setting3": true,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    }
  },

  "group1": {
    "foo": "bar",
    "baz": "bars"
  },

  "group3": {
    "fee": "100500"
  }
}
```
## Comparing two files with nested structures. The similar json report.

[![asciicast](https://asciinema.org/a/GaluLQ8BhmslsX9RHMh6GWW0v.svg)](https://asciinema.org/a/GaluLQ8BhmslsX9RHMh6GWW0v)

## Comparing two files with nested structures. The plain report.

[![asciicast](https://asciinema.org/a/9Jp5dKF3D7rAJL2nv0X7MQcbh.svg)](https://asciinema.org/a/9Jp5dKF3D7rAJL2nv0X7MQcbh)

## Comparing two files with nested structures. The json report.

[![asciicast](https://asciinema.org/a/4mnKyC7Kwt8O6JgpIF6B5zUsq.svg)](https://asciinema.org/a/4mnKyC7Kwt8O6JgpIF6B5zUsq)
