import datetime
from datetime import timedelta
x = datetime.datetime.now()
delta = x.replace(microsecond = 0)
print(delta)
