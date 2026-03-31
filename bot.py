import random
import time

def analyze_market():
    # fake logic for now (we replace later)
    decision = random.choice(["BUY", "SELL", "WAIT"])
    return decision

def run_bot():
    while True:
        signal = analyze_market()
        print(f"Signal: {signal}")
        time.sleep(5)

run_bot()
