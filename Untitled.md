```python
  
  

import logging

import threading

import datetime

import pytz

import time

import pandas as pd

import pyotp

from growwapi import GrowwFeed, GrowwAPI

  

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

ist = pytz.timezone('Asia/Kolkata')

  

# ── RSI ──────────────────────────────────────────────────────────────────────

def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:

    delta = close.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()

    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))

  

# ── Auth ──────────────────────────────────────────────────────────────────────

  
  

api_key = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjI1NjQyNzM3MTUsImlhdCI6MTc3NTg3MzcxNSwibmJmIjoxNzc1ODczNzE1LCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI4ZDY0ZjVjMy00Njg3LTQxMjMtYmFjMC1hZTRiNGNhYWU4N2ZcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiNTYxM2U0M2QtZDY3NS00MmZmLTk2MmQtODJjOWE0NzIwNGVjXCIsXCJkZXZpY2VJZFwiOlwiNTJmNGQwMWYtYjg4Zi01NjRjLTg4NWEtYjcyOGI1ZDQwMjdjXCIsXCJzZXNzaW9uSWRcIjpcIjZlNzI2M2YzLTg2NGEtNDhkMC1iODFjLTdmZWZjZTA2ZDM5M1wiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYkdEcTNKMXZYeGdEV3JjdDBGdjloa2xSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcImF1dGgtdG90cFwiLFwic291cmNlSXBBZGRyZXNzXCI6XCI0Mi42MC4xOTQuMTAzLDEwNC4yMy4xNzUuMjUxLDM1LjI0MS4yMy4xMjNcIixcInR3b0ZhRXhwaXJ5VHNcIjoyNTY0MjczNzE1MjU5LFwidmVuZG9yTmFtZVwiOlwiZ3Jvd3dBcGlcIn0iLCJpc3MiOiJhcGV4LWF1dGgtcHJvZC1hcHAifQ.VjCMJn_xuwOXoRvk6OaImuMa4D6crJgONdNdKQUb5xru4jN17Lm_wPJqpCyuu1OpEh_TmCmI6Mfbzw0O6jHeEw"

# totp can be obtained using the authenticator app or can be generated like this

totp_gen = pyotp.TOTP('OLPYPWJXTVOJFAPPNOBPI5RVAPVSLGY2')

totp = totp_gen.now()

access_token = GrowwAPI.get_access_token(api_key=api_key, totp=totp)

groww = GrowwAPI(access_token)

  

feed = GrowwFeed(groww)

# ── Instruments ───────────────────────────────────────────────────────────────

instruments_df = groww.get_all_instruments()

  

print(instruments_df.head())

nifty_cash = instruments_df[instruments_df['trading_symbol'] == "NIFTY"].iloc[0]

  

print(nifty_cash)

nearest_expiry = (

    instruments_df[

        instruments_df['trading_symbol'].str.contains("NIFTY") &

        instruments_df['exchange'].str.contains("NSE") &

        instruments_df['segment'].str.contains("FNO")

    ]['expiry_date'].min()

)

print(f"Nearest expiry: {nearest_expiry}")

  

option_chain = groww.get_option_chain(

    exchange=groww.EXCHANGE_NSE,

    underlying="NIFTY",

    expiry_date=nearest_expiry

)

CE_option_tokens = {s: v['CE']['trading_symbol'] for s, v in option_chain['strikes'].items()}

PE_option_tokens = {s: v['PE']['trading_symbol'] for s, v in option_chain['strikes'].items()}

  
  
  

# ── Shared state ──────────────────────────────────────────────────────────────

_ltp_lock   = threading.Lock()

_ltp_value  = None

candle_df   = pd.DataFrame(columns=['time', 'LTP']).set_index('time')

in_trade    = False

last_candle_time: datetime.time | None = None

  

def get_ltp():

    with _ltp_lock:

        return _ltp_value

  

def set_ltp(val):

    with _ltp_lock:

        global _ltp_value

        _ltp_value = val

  

# ── Order helpers ─────────────────────────────────────────────────────────────

LOT_SIZE = 65

  

def market_sell(symbol: str):

    return groww.place_order(

        exchange=groww.EXCHANGE_NSE,

        segment=groww.SEGMENT_FNO,

        trading_symbol=symbol,

        transaction_type=groww.TRANSACTION_TYPE_SELL,

        quantity=LOT_SIZE,

        order_type=groww.ORDER_TYPE_MARKET,

        product_type=groww.PRODUCT_MIS,

    )

  

def sl_buy(symbol: str, entry_price: float):

    """Buy stop-loss at 1.5× the entry price."""

    trigger = round(entry_price * 1.5, 1)

    limit   = round(trigger * 1.01, 1)          # small buffer above trigger

    return groww.place_order(

        exchange=groww.EXCHANGE_NSE,

        segment=groww.SEGMENT_FNO,

        trading_symbol=symbol,

        transaction_type=groww.TRANSACTION_TYPE_BUY,

        quantity=LOT_SIZE,

        order_type=groww.ORDER_TYPE_STOP_LOSS,

        product_type=groww.PRODUCT_MIS,

        price=limit,

        trigger_price=trigger,

    )

  

def place_short_straddle_with_sl(ltp: float):

    atm  = int(ltp // 50 * 50)

    atm2 = atm + 50

    logging.info(f"ATM strikes: {atm}, {atm2}")

  

    for strike in (atm, atm2):

        for token_map, label in ((CE_option_tokens, 'CE'), (PE_option_tokens, 'PE')):

            sym = token_map[strike]

            market_sell(sym)

            logging.info(f"Sold {label} {strike}: {sym}")

            entry_price = groww.get_quote(

                exchange=groww.EXCHANGE_NSE,

                segment=groww.SEGMENT_FNO,

                trading_symbol=sym,

            )['last_price']

            sl_buy(sym, entry_price)

            logging.info(f"SL placed for {label} {strike} @ {entry_price * 1.5:.1f}")

  

# ── Square-off all open MIS positions ─────────────────────────────────────────

def square_off_all():

    logging.info("Squaring off all MIS positions at market close.")

    positions = groww.get_positions()          # adjust to actual API method

    for pos in positions.get('data', []):

        if pos.get('product') == 'MIS' and pos.get('net_quantity', 0) != 0:

            qty  = abs(pos['net_quantity'])

            side = (groww.TRANSACTION_TYPE_SELL

                    if pos['net_quantity'] > 0

                    else groww.TRANSACTION_TYPE_BUY)

            groww.place_order(

                exchange=pos['exchange'],

                segment=pos['segment'],

                trading_symbol=pos['trading_symbol'],

                transaction_type=side,

                quantity=qty,

                order_type=groww.ORDER_TYPE_MARKET,

                product_type=groww.PRODUCT_MIS,

            )

  

# ── Candle / RSI logic (called from feed callback) ───────────────────────────

def maybe_close_candle(ltp: float):

    """

    Called on every tick. Closes a 3-min candle when the minute is a multiple

    of 3 and we haven't already closed this candle.

    """

    global candle_df, in_trade, last_candle_time

  

    now      = datetime.datetime.now(ist)

    # Market close: square off 5 min before end

    if now.time() >= datetime.time(15, 20):

        if in_trade:

            square_off_all()

            in_trade = False

        return

  

    if now.minute % 3 != 0:

        return

  

    candle_ts = now.replace(second=0, microsecond=0).time()

    if candle_ts == last_candle_time:

        return                               # already processed this candle

  

    last_candle_time = candle_ts

    new_row = pd.DataFrame({'LTP': [ltp]}, index=[candle_ts])

    candle_df = pd.concat([candle_df, new_row])

    candle_df['RSI'] = compute_rsi(candle_df['LTP'], 14)

    logging.info(f"Candle @ {candle_ts}  LTP={ltp:.2f}  RSI={candle_df['RSI'].iloc[-1]:.2f}")

  

    # Need at least 15 candles for a reliable RSI, and 2 to detect crossover

    if len(candle_df) < 15:

        return

    if in_trade:

        return

  

    rsi_now  = candle_df['RSI'].iloc[-1]

    rsi_prev = candle_df['RSI'].iloc[-2]

  

    crossed_back_from_overbought = rsi_prev >= 70 and rsi_now < 70

    crossed_back_from_oversold   = rsi_prev <= 30 and rsi_now > 30

  

    if crossed_back_from_overbought or crossed_back_from_oversold:

        logging.info(f"RSI crossover detected: {rsi_prev:.2f} → {rsi_now:.2f}")

        try:

            place_short_straddle_with_sl(ltp)

            in_trade = True

        except Exception as e:

            logging.error(f"Order placement failed: {e}")

  

# ── Feed callback ─────────────────────────────────────────────────────────────

def on_data_received(meta):

    print(feed.get_index_value())

    if (meta['exchange']       == groww.EXCHANGE_NSE and

        meta['segment']        == groww.SEGMENT_CASH and

        meta['exchange_token'] == nifty_cash['exchange_token']):

  

        ltp = feed.get_index_value(

            exchange=groww.EXCHANGE_NSE,

            segment=groww.SEGMENT_CASH,

            exchange_token=nifty_cash['exchange_token'],

        )

        if ltp is None:

            return

        set_ltp(ltp)

        maybe_close_candle(ltp)             # ← all logic lives here

  

# ── Start ─────────────────────────────────────────────────────────────────────

feed = GrowwFeed(groww)

instruments_list = [{

    "exchange": "NSE",

    "segment":  "CASH",

    "exchange_token": nifty_cash['exchange_token'],

}]

  

result = feed.subscribe_index_value(instruments_list, on_data_received=on_data_received)

print("Subscribe result:", result)

logging.info("Feed started. consume() is now the event loop.")

feed.consume()   # blocks here — all logic runs inside on_data_received
```