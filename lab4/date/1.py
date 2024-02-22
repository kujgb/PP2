from datetime import datetime, timedelta

current = datetime.now()
date = datetime.now() - timedelta(5)
print("CURRENT DATE: ", current.strftime("%Y-%m-%d"))
print("DATE BEFORE 5 DAYS: ", date.strftime("%Y-%m-%d"))