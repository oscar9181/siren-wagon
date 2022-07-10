
from cmath import exp
import requests
from payments.models import DarajaToken
from payments.daraja_auth import request_new_token
from decouple import config
import json


def initiate_transaction(sender, receiver, amount, message):
    token, expired = DarajaToken.get_credentials()
    if expired:
        new_token, expiry = request_new_token()
        print("New token: ", new_token, expiry)
        updated_token = token.update_token(new_token)
        token = updated_token
    headers = {
        'Authorization': f'Bearer {token.token}'

    }

    payload = {
        "BusinessShortCode": 174379,
        "Password": config("DARAJA_PASSWORD"),
        "Timestamp": "20220710230712",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254708374149,
        "PartyB": 600000,
        "PhoneNumber": 254708374149,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    }
    # {
    #     "BusinessShortCode": 174379,
    #     "Password": config("DARAJA_PASSWORD"),
    #     "Timestamp": "20220710132848",
    #     "TransactionType": "CustomerPayBillOnline",
    #     "Amount": amount,
    #     "PartyA": sender.phone,
    #     "PartyB": 174379,
    #     "PhoneNumber": receiver.account_holder.phone,
    #     "CallBackURL": "https://mydomain.com/path",
    #     "AccountReference": "Siren Wagon",
    #     "TransactionDesc": message
    # }

    response = requests.request(
        'POST', config('MPESA_EXPRESS'), headers=headers, data=payload)
    print(response.text.encode('utf-8'))
    return json.loads(response.text.encode('utf-8'))
