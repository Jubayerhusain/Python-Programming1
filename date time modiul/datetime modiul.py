import datetime
n=datetime.datetime.now()
t=datetime.datetime.today()
u=datetime.datetime.utcnow()
print("Now date and time:",n)
print("today date and time:",t)
print("UTC now date and time:",u)


import datetime
t=datetime.time(12,21,34)
print("Time is :",t)
d=datetime.date.today()
print("Date is :",d)
dt=datetime.datetime.combine(d,t)
print("Date & time is :",dt)

