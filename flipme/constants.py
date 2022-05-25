#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""flipme

File: flipme/constants,py
Author: Havocesp <https://github,com/havocesp/flipme>
Created: 2022-05-24
"""
ORDER_STATUS = [
    'WAITING_FOR_DEPOSIT',
    'DEPOSIT_RECEIVED',
    'DEPOSIT_CONFIRMED',
    'EXECUTED',
    'NEEDS_REFUND',
    'REFUNDED',
    'CANCELED',
    'EXPIRED'
]

PAYMENT_STATUS = [
    'PENDING',
    'UNDERPAY_RECEIVED',
    'UNDERPAY_CONFIRMED',
    'PAYMENT_RECEIVED',
    'PAYMENT_CONFIRMED',
    'OVERPAY_RECEIVED',
    'OVERPAY_CONFIRMED'
]
