#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""flipme

File: flipme/utils.py
Author: Havocesp <https://github.com/havocesp/flipme>
Created: 2022-05-24
"""


def _clean_params(params, *drop_args):
    drop_args = ['self', 'cls', *drop_args]
    return {k: v for k, v in params.items() if v and k[0] != '_' and k not in drop_args}
