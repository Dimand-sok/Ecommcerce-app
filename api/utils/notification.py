

class notification:
    def send():
        pass
    
class SMSnotification(notification):
    def send(self):
        print("send via SMS")
        
class Emailnotification(notification):
    def send(self):
        print("send via Email")
        
def get_notification(type="email"):
    notification = dict(sms=SMSnotification(), email=Emailnotification())
    return notification.get(type, None)