from requests import post
from json import dumps


class notification:
    def send():
        pass
    
class SMSnotification(notification):
    def __init__(self):
        self.__secret = "$5$rounds=535000$fuc/qVmBUzfts8j1$lbfY6hFhWU1roQiwJslGTGssKjgFHkFh3HuwO5ULkE."
        self.__private = "Z79K6r2tE-mEVe_qQyElExjQMbl9GgIc6XfAF8Wfhc0WTXfTapB-K9_3SYeQUTCBscANEhmh99LxT9nvTjwzrg"
        self.headers = {"X-Secret": self.__secret, "Content-Type": "application/json"}
        self.getway_endpoint = "https://cloudapi.plasgate.com/rest/send"
    
    def send(self, **kwargs):
        content = "Your verification code {otp}".format(otp=kwargs.get("otp"))
        body = {"sender": "SMS Info", "to": kwargs.get("phone"), "content": content}
        
        resp = post(self.getway_endpoint,params={"private_key": self.__private},headers=self.headers,json=body,verify=False)
        
        if resp.status_code == 200:
            print(resp.content)
        else:
            print(resp.__dict__)
        
class Emailnotification(notification):
    def send(self):
        print("send via Email")
        
def get_notification(type="email"):
    notification = dict(sms=SMSnotification(), email=Emailnotification())
    return notification.get(type, None)