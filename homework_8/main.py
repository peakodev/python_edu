from collections import defaultdict
from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    today = date.today()
    start_day = today - timedelta(days=(today.weekday() - 5) % 7) if today.weekday() == 0 else today

    available_days = {}
    for i in range(7):
        available_days[(start_day.month, start_day.day)] = start_day.strftime("%A")
        start_day += timedelta(days=1)

    available_days = {k: 'Monday' if v in ['Saturday', 'Sunday'] else v for k, v in available_days.items()}

    show_sets_of_birth = defaultdict(list)
    for user in users:
        birth = user["birthday"]
        if (birth.month, birth.day) in available_days.keys():
            show_sets_of_birth[available_days[(birth.month, birth.day)]].append(user['name'])

    return show_sets_of_birth


if __name__ == "__main__":
    test_users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 10).date()},
        {"name": "Nazar", "birthday": datetime(1988, 1, 15).date()},
    ]

    result = get_birthdays_per_week(test_users)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")