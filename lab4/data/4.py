import datetime
from datetime import timedelta
x = datetime.datetime.now()
x1 = timedelta(seconds = 54040)
delta = x - x1
print(delta.strftime("%S"))
