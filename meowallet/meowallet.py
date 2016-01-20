import json
import requests

from exceptions import CheckoutException


class Wallet(object):
    """
    """

    API_ENDPOINT = ''
    authorization_header = "WalletPT " + APIKEY

    def __init__(self, api_key, url_confirm, url_cancel,
                 endpoint='https://services.wallet.pt/api/v2/'):
        self.API_KEY = api_key
        self.authorization_header = "WalletPT " + api_key
        self.endpoint = endpoint

    def checkout(self, transaction_id, client, items, ammount, currency="EUR"):
        """ Create the checkout data structure and send it to the API,
            after validation
        """

        payload = {
            "payment": {
                "client" : client,
                "amount" : amount,
                "currency": currency,
                "items" : items
            },
            "url_confirm" : url_confirm,
            "url_cancel": url_cancel,
        }

        response = requests.post(self.endpoint + "checkout",
                                 data=json.dumps(payload),
                                 headers=headers)

        data = response.json()
        if response.status_code == requests.codes.ok:
            return data
        else:
            raise CheckoutException(data['code'], data['message'], data)

