import datetime
from datetime import timedelta
today = datetime.datetime.now()
yest = today - timedelta(days = 1)
tomm = today + timedelta(days = 1)
print(yest.strftime('%A'))
print(yest.strftime('%d '))
print(today.strftime('%A'))
print(today.strftime('%d '))
print(tomm.strftime('%A'))
print(tomm.strftime('%d '))