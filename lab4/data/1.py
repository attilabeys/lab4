import datetime
from datetime import timedelta
x = datetime.datetime.now()
res = x - timedelta(days = 5)
print(res.strftime('%A'))
print(res.strftime('%d '))