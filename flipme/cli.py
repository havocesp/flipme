#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""flipme

File: flipme/cli.py
Author: Havocesp <https://github.com/havocesp/flipme>
Created: 2022-05-24
"""
import sys
from argparse import ArgumentParser
from pprint import pprint

from flipme import Flypme


def cmd_create(args):
    response = Flypme().new_order(**vars(args))
    pprint(response)


if __name__ == '__main__':
    sys.argv.extend(['new', '-f', 'ETH', '-t', 'XMR'])
    ap = ArgumentParser()

    sbp = ap.add_subparsers(help='Sub commands')

    sp_create = sbp.add_parser('new')

    sp_create.add_argument('--from-currency', '-f', help='Source currency.')
    sp_create.add_argument('--to-currency', '-t', help='Destination currency.')
    sp_create.add_argument('--amount', '-a', type=float, help='Amount to exchange.')
    sp_create.add_argument('--destination', '-d', help='Destination address.')
    sp_create.add_argument('--refund-address', '-r', help='Refund address currency.')
    sp_create.add_argument('--referal_code', '-c', help='Referal code.')

    sp_create.set_defaults(func=cmd_create)

    cli_args = ap.parse_args()

    if hasattr(cli_args, 'func'):
        fn = getattr(cli_args, 'func')
        delattr(cli_args, 'func')
        fn(cli_args)
    else:
        ap.print_help()
