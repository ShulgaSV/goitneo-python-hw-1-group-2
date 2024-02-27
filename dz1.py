


from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week_start = today + timedelta(days=(7 - today.weekday()))
    next_week_end = next_week_start + timedelta(days=7)
    
    birthdays = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days < 7:
            # Визначення дня тижня та перенесення на понеділок, якщо день народження вихідний
            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_weekday in ["Saturday", "Sunday"]:
                birthday_weekday = "Monday"
            # Збереження імені користувача за відповідним днем тижня
            birthdays[birthday_weekday].append(name)
    
    print("Birthdays for next week:")
    for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": datetime(1985, 5, 15)},
    {"name": "Jane Smith", "birthday": datetime(1990, 8, 25)},
    {"name": "Alice Johnson", "birthday": datetime(1978, 9, 10)},
    {"name": "Bob Brown", "birthday": datetime(1982, 4, 5)}
]

get_birthdays_per_week(users)