from datetime import datetime


def get_days_in_month(month, year):
    date = datetime(year=year, month=month, day=1)
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if next_month == 1 else year
    return (datetime(year=next_year, month=next_month, day=1) - date).days


print(get_days_in_month(12, 2012))