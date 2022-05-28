import datetime as dt
import time
import logging

from optibook.synchronous_client import Exchange

from math import floor, ceil
from black_scholes import call_value, put_value, call_delta, put_delta
from libs import calculate_current_time_to_date

exchange = Exchange()
exchange.connect()

logging.getLogger('client').setLevel('ERROR')


STOCK_ID = 'BMW'
OPTIONS = [
    {'id': 'BMW-20220318-050C', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 50, 'callput': 'call'},
    {'id': 'BMW-20220318-050P', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 50, 'callput': 'put'},
    {'id': 'BMW-20220318-075C', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 75, 'callput': 'call'},
    {'id': 'BMW-20220318-075P', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 75, 'callput': 'put'},
    {'id': 'BMW-20220318-100C', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 100, 'callput': 'call'},
    {'id': 'BMW-20220318-100P', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 100, 'callput': 'put'},
    {'id': 'BMW-20220318-125C', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 125, 'callput': 'call'},
    {'id': 'BMW-20220318-125P', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 125, 'callput': 'put'},
    {'id': 'BMW-20220318-150C', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 150, 'callput': 'call'},
    {'id': 'BMW-20220318-150P', 'expiry_date': dt.datetime(2022, 3, 18, 12, 0, 0), 'strike': 150, 'callput': 'put'},
]


while True:
    print(f'')
    print(f'-----------------------------------------------------------------')
    print(f'TRADE LOOP ITERATION ENTERED AT {str(dt.datetime.now()):18s} UTC.')
    print(f'-----------------------------------------------------------------')

    # TODO: Determine stock value

    # For each option
    for option in OPTIONS:
        # Print which option we are updating
        print(f'''Updating option {option['id']} with expiry date {option['expiry_date']}, strike {option['strike']} '''
              f'''and type {option['callput']}.''')

        # TODO: Delete existing orders

        # TODO: Calculate option value

        # TODO: Calculate desired bid and ask prices

        # TODO: Insert limit orders on those prices for a desired volume

        # Wait 1/10th of a second to avoid breaching the exchange frequency limit
        time.sleep(0.10)

    # TODO: Calculate current delta position across all instruments
    # TODO: Calculate stocks to buy/sell to become close to delta-neutral
    # TODO: Perform the hedging stock trade by inserting an IOC order on the stock against the current top-of-book

    # Sleep until next iteration
    print(f'\nSleeping for 4 seconds.')
    time.sleep(4)
