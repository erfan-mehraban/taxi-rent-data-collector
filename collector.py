from requests import Session

class PriceCollector:

    def __init__(self, token, session: Session, alias: str):
        self.token = token
        self.session = session
        self.alias = alias
    
    @classmethod
    def inital_with_token(cls, token: str):
        raise NotImplementedError

    def get_price(self, start_cordinate, dest_cordinate):
        raise NotImplementedError

class PriceManipulator:

    def __init__(self):
        self.collectors = list()

    def add_app(self, price_collector: PriceCollector, token: str):
        self.collectors.append(
            price_collector.inital_with_token(token)
        )

    def get_all_prices(self, start_cordinate, dest_cordinate):
        prices = {}
        for c in self.collectors:
            prices[c.alias] = c.get_price(start_cordinate, dest_cordinate)
        return prices