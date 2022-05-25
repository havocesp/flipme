# Flip.me Python API wrapper

## Description

A __Flip.me__ crypto exchange Python 3 API wrapper.

## Requirements

This project require the following dependencies:

- Python 3.9 (lower or upper versions not tested)
- __requests_~~_~~

## Changelog

- [__24-05-2022__] [__v0.0.1__] Intial version.

## Usage

```python
from pprint import pprint
from flipme import Flypme

api = Flypme()
result = api.new_order('BTC', 'ZEC', 0.1, 'LajyQBeZaBA1NkZDeY8YT5RYYVRkXMvb2T')
pprint(result)
```
