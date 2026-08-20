#!/usr/bin/env python3
import requests
# Simple crypto price alert
print('BTC:', requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()['bitcoin']['usd'])
