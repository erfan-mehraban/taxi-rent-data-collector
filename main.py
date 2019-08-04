from datetime import datetime
import schedule
import sys
from collector import PriceManipulator
from config import load_config
from data_store import save_record
from tap30 import Tap30
from snapp import Snapp
from time import sleep

#initialize
config_path = 'config.yaml'
if len(sys.argv) == 2:
    config_path = sys.argv[1]
config = load_config(config_path)
pm = PriceManipulator()
pm.add_app(Snapp, config['snapp_token'])
pm.add_app(Tap30, config['tap30_token'])

def collect_prices():
    error_occurred = True
    while error_occurred:
        try:
            app_price = pm.get_all_prices(config['start_cordinate'], config['dest_cordinate'])
            for app_name, price in app_price.items():
                print(datetime.now().strftime("%H:%M"), app_name, price)
                save_record(price, config['result_store_path'][app_name])
            error_occurred = False
        except Exception as e:
            print(e)
            error_occurred = True
            sleep(1)

# schedule
schedule.every(config['get_price_intervals']).minutes.do(collect_prices)
while True:
    schedule.run_pending()
    sleep(1)