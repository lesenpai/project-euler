from datetime import date, timedelta

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)
delta = end_date - start_date

n = 0
for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    if day.day == 1 and day.strftime('%a') == 'Sun':
        n += 1
print(n)