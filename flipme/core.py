#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""flipme

File: flipme/core.py
Author: Havocesp <https://github.com/havocesp/flipme>
Created: 2022-05-24
"""
import json
from typing import Dict

import requests

from utils import _clean_params


class Flypme:

    def __init__(self, api_version: str = None):
        self._headers = {'Content-type': 'application/json'}
        api_version = str(api_version or "1").lower().strip(' v')
        self._url = f'https://flyp.me/api/v{api_version}'

    def _request(self, end_point: str, method: str = None, **params):
        method = str(method or 'get').lower()
        request_params = {
            'url': f'{self._url}/{end_point}',
            'method': method,
            'headers': self._headers,
            'timeout': (30, 30)
        }

        if params:
            if method == 'get' and params:
                request_params.update(params=params)
            elif method in ('post', 'delete', 'put'):
                request_params.update(data=json.dumps(params))

        response = requests.request(**request_params)

        if response.ok:
            return response.json()
        elif 'json' in str(response.headers).lower():
            return response.json()
        else:
            response.raise_for_status()

    def _get(self, end_point: str, **params):
        return self._request(end_point, 'get', **params)

    def _post(self, end_point: str, **params):
        return self._request(end_point, 'post', **params)

    def new_order(self, from_currency: str, to_currency: str, amount: float, destination: str, refund_address: str = None, is_invoice=False, referal_code: str = None):
        """Initiate a new order.

        On the initial request "invoiced_amount" can also be specified instead of ordered_amount.

        You can optionally specify "destination" and "refund_address" on the request.

        You can optionally specify "referral_code" on the request. Note you will need to use a validated referral code or the order will fail.

        :param from_currency:
        :param to_currency:
        :param ordered_amount:
        :param destination:
        :param refund_address:
        :param is_invoice:
        :param referal_code:
        :return:
        """
        params = _clean_params(locals(), 'is_invoice')
        if is_invoice:
            params.update(invoice_amount=params.pop('amount'))
        else:
            params.update(ordered_amount=params.pop('amount'))
        # params = {
        #     'from_currency': from_currency,
        #     'to_currency': to_currency,
        #     'invoice_amount' if is_invoice else 'ordered_amount': f'{amount}',
        #     'destination': destination
        # }
        #
        # if refund_address:
        #     params.update(resfund_address=refund_address)
        # if referal_code:
        #     params.update(referal_code=referal_code)

        return self._post('order/create', order=params)

    def check_order(self, uuid):
        """Check order status by uuid.

        :param uuid: order unique ID.
        :return:
        """
        return self._post('order/check', uuid=uuid)

    def update_order(self, uuid: str, order_amount: float = None, destination: str = None, refund_address: str = None, referral_code=None):
        """Update an order.

        :param uuid: order unique ID.
        :param order_amount:
        :param destination:
        :param refund_address:
        :return:
        """
        assert order_amount or destination or refund_address, 'At least an order amount or destination/refund address must be supplied.'
        params = {
            'uuid': uuid,
            'ordered_amount': f'{order_amount}',
            'destination': destination,
            'refund_address': refund_address,
            'referral_code': referral_code
        }
        params = _clean_params(params)
        return self._post('order/update', order=params)

    def add_order_refund_address(self, uuid, address):
        """Add a refund address for orders not having one.

        :param uuid: order unique ID.
        :param address:
        :return:
        """
        resp = self._post('order/addrefund', uuid=uuid, address=address)
        if isinstance(resp, dict) and 'result' in resp and resp['result'] == 'ok':
            return True
        else:
            return resp

    def get_order_info(self, uuid):
        """Get order full info.

        This command is rate limited so you should not use for continuous monitoring of an order, use 'check' instead.

        :param uuid: order unique ID.
        :return:
        """
        return self._post('order/info', uuid=uuid)

    def cancel_order(self, uuid) -> Dict:
        """Cancel a pending order.


        :param uuid: order unique ID.
        :return:
        """
        return self._post('order/cancel', uuid=uuid)

    def accept_order(self, uuid):
        """Accept an order.

    Response example:
    >>> response_data = {
    >>>   "order": {
    >>>     "uuid": "eeeeb105-d30d-43f1-bbb8-a9f8a237acf5",
    >>>     "destination": "t1SBTywpsDMKndjogkXhZZSKdVbhadt3rVt",
    >>>     "exchange_rate": "0.4888796682",
    >>>     "ordered_amount": "0.02",
    >>>     "invoiced_amount": "0.04213716",
    >>>     "charged_fee": "0.0006",
    >>>     "from_currency": "LTC",
    >>>     "to_currency": "ZEC"
    >>>   },
    >>>   "expires": 1145,
    >>>   "deposit_address": "M88aw1wCKvVP7EAmqviV8ggxM5ds8BypvQ",
    >>>   "refund_address": "LajyQBeZaBA1NkZDeY8YT5RYYVRkXMvb2T"
    >>> }

        :param uuid: order unique ID.
        :return:
        """
        return self._post('order/accept', uuid=uuid)

    @property
    def exchange_rates(self, referral_code=None):
        """Get exchange rates.

        Example result:
        >>> response_data = {
        >>> "LTC-BTC":"0.0156975877",
        >>> "BTC-LTC":"60.5139402396",
        >>> "PPC-BTC":"0.0004053465",
        >>> "PPC-LTC":"0.024900034",
        >>> "BTC-PPC":"2338.8025331034 (...)"
        >>> }


        :param referral_code:
        :return:
        """
        params = _clean_params(locals())
        return self._get('data/exchange_rates', **params)

    @property
    def active_currencies(self):
        """Get available currencies information.

        >>> response_data = {
        >>> "BTC":  {
        >>>     "code": "BTC",
        >>>     "precision": 8,
        >>>     "display_precision": 4,
        >>>     "created_at": "2014-02-04T02:28:37.000Z",
        >>>     "updated_at": "2017-10-20T14:02:11.000Z",
        >>>     "name": "Bitcoin",
        >>>     "website": "https://bitcoin.org/",
        >>>     "confirmation_time": 20,
        >>>     "default": False,
        >>>     "charged_fee": "0.0006",
        >>>         "currency_type": "CRYPTO",
        >>>         "exchange": True,
        >>>         "send": True
        >>>     }
        >>> }

        :return:
        """
        return self._get('currencies')

    def get_order_limits(self, from_currency, to_curency):
        """Get max and min limits in "to_currency".

        Example response:
        >>> {"min":"0.015","max":"52.11198655"}

        :param from_currency:
        :param to_curency:
        :return:
        """
        return self._get(f'order/limits/{from_currency}/{to_curency}')


if __name__ == '__main__':
    from pprint import pprint

    active_currencies = Flypme().active_currencies
    pprint(active_currencies)
