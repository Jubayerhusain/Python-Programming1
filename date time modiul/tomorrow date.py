from datetime import date
from datetime import timedelta
def tomorrow():
    today=date.today()
    tomorrow=date.today()+timedelta(days=1)
    return tomorrow
print("Today's Date Is :",date.today())
print("Tomorrow Date Will Be :",tomorrow())