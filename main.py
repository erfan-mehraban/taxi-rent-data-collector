import schedule
from collector import PriceManipulator
from config import *
from data_store import save_record
from tap30 import Tap30
from snapp import Snapp
from time import sleep

#initialize
pm = PriceManipulator()
pm.add_app(Snapp, snapp_token)
pm.add_app(Tap30, tap30_token)

def collect_prices():
    try:
        app_price = pm.get_all_prices(start_cordinate, dest_cordinate)
        for app_name, price in app_price.items():
            save_record(app_name, price)
    except Exception as e:
        print(e)

# schedule
schedule.every(30).minutes.do(collect_prices)
while True:
    schedule.run_pending()
    sleep(1)