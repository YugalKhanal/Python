from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1

print(duration)
print("days", duration.days)
print("duration", duration.seconds)
