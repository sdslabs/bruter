# bruter

A rule based string bruteforcer. Similar to [brute](https://pypi.org/project/brute/) but more versatile.

## Overview

Bruter provides a callback based bruteforce interface. Mainly a single function `brute` is exported:

```python
brute(fmt, callback=None, symbols={})
```

- `fmt`: The string to be plugged variables into
- `callback`: This is the function which will be called for every terminal value
- `symbols`: This is a `dict` which maps symbols (which are strings) to a list of values

## Example

```python
from bruter import brute

def printer(x):
	print(x)

symbols = {
	'H': ['a', 'b', 'c'],
	'L': ['x', 'y'],
	'X': ['1', '2']
}

brute("hello <H> <L> <X>", printer, symbols)

```

This one gives you output --

```
hello a x 1
hello a x 2
hello a y 1
hello a y 2
hello b x 1
hello b x 2
hello b y 1
hello b y 2
hello c x 1
hello c x 2
hello c y 1
hello c y 2
```

You can also use the predefined strings inside the `string` module in Python 3 for defining symbols

```python
from bruter import brute
import string

def printer(x):
	print(x)

symbols = {
	'H': string.ascii_lowercase
}

brute("hello <H>", printer, symbols)

```
which gives output --

```
hello a
hello b
hello c
hello d
hello e
hello f
hello g
hello h
hello i
hello j
hello k
hello l
hello m
hello n
hello o
hello p
hello q
hello r
hello s
hello t
hello u
hello v
hello w
hello x
hello y
hello z
```
