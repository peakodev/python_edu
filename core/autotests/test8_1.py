from datetime import datetime


def get_days_from_today(date):
    splitted_date = date.split('-')
    to_date = datetime(
        year=int(splitted_date[0]),
        month=int(splitted_date[1]),
        day=int(splitted_date[2])
    )
    return (datetime.now() - to_date).days


print(get_days_from_today('2025-10-11'))