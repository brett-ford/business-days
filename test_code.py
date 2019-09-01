import datetime as dt
from n_business_days import n_business_days


"""Test Code:"""

today = dt.date.today()
print('Today: {}'.format(today))
for n in range(-5, 6):
    print('{}: {}'.format(n, n_business_days(today, n)))
print()


for d in range(1, 16):
    today = dt.date(2019, 6, d)
    print('+0: {}'.format(today))
    print('+3: {}'.format(n_business_days(today, 3)))
    print()

for y in range(2018, 2020):
    for m in range(1, 13):
        for d in range(1, 28):
            today = dt.date(y, m, d)
            print('+0: {}'.format(today))
            print('-2: {}'.format(n_business_days(today)))
            print()
