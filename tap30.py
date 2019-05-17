from requests import Session
from collector import PriceCollector

class Tap30(PriceCollector):

    @classmethod
    def inital_with_token(cls, token):
        return cls(token, Session(), "tap30")
        
    def get_price(self, start_cordinate, dest_cordinate,):
        data = {"origin": {"latitude":start_cordinate[0],"longitude":start_cordinate[1]},
                "destinations":[{"latitude":dest_cordinate[0],"longitude":dest_cordinate[1]}],
                "hasReturn":False,"initiatedVia":"WEB"}

        headers = {
            'x-authorization': self.token
        }

        r = self.session.post(
            'https://tap33.me/api/v2.1/ride/preview',
            json=data,
            cookies=None,
            headers=headers)
        if r.status_code >= 200 or r.status_code < 300:
            parsed = r.json()["data"]
            return parsed['serviceCategoriesInfo'][0]['priceInfos'][0]["price"]
        raise Exception()
