from fastapi import FastAPI, Header, HTTPException, Query
from typing import Optional
from pydantic import BaseModel
import requests 
import config

app = FastAPI()

@app.get("/account_details")
async def account_details():
    accountId = config.id
    url = "https://api-sandbox.poweredbyibex.io/v2/account/"+accountId

    headers = {
        "accept": "application/json",
        "Authorization": config.auth
    }

    response = requests.get(url, headers=headers)
    return {
        "response": response.json()
    }

@app.post("/create_invoice")
async def create_invoice(amount: float, memo: str, webhook_url, webhook_secret):
    url = "https://api-sandbox.poweredbyibex.io/v2/invoice/add"

    payload = {
    "expiration": 900,
    "amount": amount,
    "accountId": config.id,
    "memo": memo,
    "webhook": webhook_url,
    "webhook_secret": webhook_secret

    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": config.auth
    }

    response = requests.post(url, json=payload, headers=headers)

    return {
        "response": response.json()
    }


@app.post("/pay_invoice")
async def pay_invoice(amount: float, webhook_url, webhook_secret, bolt11:str):
    url = "https://api-sandbox.poweredbyibex.io/v2/invoice/pay"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": config.auth
    }

    payload = {
        "amount": amount,
        "accountId": config.id,
        "webhook": webhook_url,
        "webhook_secret": webhook_secret,
        "bolt11": bolt11

    }

    response = requests.post(url,  json=payload, headers=headers)

    return {
        "response": response.json()
    }