from datetime import datetime, time
def date(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2022-05-17 08:09:52', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
print("\n%d seconds" %(date(date2, date1)))