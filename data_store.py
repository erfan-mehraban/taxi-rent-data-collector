from config import result_store_path
from datetime import datetime
def save_record(service_alias: str, price: int):
    path = result_store_path[service_alias]
    with open(path, 'a') as fh:
        dt = datetime.now().strftime("%d-%m-%Y %H:%M")
        week_day = datetime.now().strftime("%a")
        time = datetime.now().strftime("%H:%M")
        record = f"{dt},{week_day},{time},{price}\n"
        fh.write(record)

