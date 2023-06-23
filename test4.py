from datetime import datetime, timedelta

now = datetime.now()

print(now)

now_year = now.year
now_month = now.month
next_month = now + timedelta(days=30)
month = now.strftime('%m')
month2 = next_month.strftime('%m')

print(f'{now_year}-{month}')
print(f'{now_year}-{month2}')




