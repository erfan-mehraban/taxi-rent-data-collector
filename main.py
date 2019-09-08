from datetime import datetime
import schedule
import sys
from collector import PriceManipulator
from config import load_config
from data_store import save_record
from tap30 import Tap30
from snapp import Snapp
from time import sleep
from wait_time_calculator import waitTimeCalculator

#initialize
config_path = 'config.yaml'
if len(sys.argv) == 2:
    config_path = sys.argv[1]
config = load_config(config_path)
pm = PriceManipulator()
pm.add_app(Snapp, config['snapp_token'])
pm.add_app(Tap30, config['tap30_token'])

def collect_prices():
    first_try = True
    wt = waitTimeCalculator()
    while wt.still_error() or first_try:
        first_try = False
        try:
            app_price = pm.get_all_prices(config['start_cordinate'], config['dest_cordinate'])
            for app_name, price in app_price.items():
                print(datetime.now().strftime("%H:%M"), app_name, price)
                save_record(price, config['result_store_path'][app_name])
            wt.reset()
        except Exception as e:
            print(e)
            wt.count_error()
            sleep_time = wt.get_wait_time()
            print(f"waiting {sleep_time} seconds.")
            sleep(sleep_time)

# schedule
schedule.every(config['get_price_intervals']).minutes.do(collect_prices)
while True:
    schedule.run_pending()
    sleep(1)