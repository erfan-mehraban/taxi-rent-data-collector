from requests import Session
from collector import PriceCollector

class Snapp(PriceCollector):

    # @classmethod
    # def login(cls, username, password):
    #     '''
    #     Not Working
    #     '''
    #     data = {
    #         'username': username,
    #         'password': password
    #     }
    #     s = Session()
    #     r = s.post(
    #         'https://web-api.snapp.ir/api/v1/auth/login',
    #         json=data,
    #         cookies=None
    #     )
    #     print(r.content)
    #     if r.status_code >= 200 or r.status_code < 300:
    #         t = r.json()['token']
    #         return cls(t, s, "snapp")
    #     raise Exception(r)

    @classmethod
    def inital_with_token(cls, token):
        return cls(token, Session(), "snapp")

    def get_price(self, start_cordinate, dest_cordinate, rount_trip=0, waiting=0):
        data = {
            'origin_lat': start_cordinate[0],
            'origin_lng': start_cordinate[1],
            'destination_lat': dest_cordinate[0],
            'destination_lng': dest_cordinate[1],
            'round_trip': rount_trip,
            'waiting': waiting
        }

        headers = {
            'Authorization': self.token
        }

        r = self.session.post(
            'https://web-api.snapp.ir/api/v1/ride/price',
            json=data,
            cookies=None,
            headers=headers)
        if r.status_code >= 200 or r.status_code < 300:
            prices = r.json()['prices']
            return prices[0]["final"] // 10 # rial to toman
        raise Exception()
