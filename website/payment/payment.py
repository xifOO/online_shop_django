import random
import pyqiwip2p
from settings import temp


SECRET_QIWI_KEY = temp.SECRET_QIWI_KEY
new_bill = random.randrange(1, 9999999999999999999)
p2p = pyqiwip2p.QiwiP2P(auth_key=SECRET_QIWI_KEY)


def pay(amount):
    global new_bill, p2p
    new_bill = p2p.bill(bill_id=new_bill, amount=amount, lifetime=15)
    return new_bill.pay_url






