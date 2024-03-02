# реалізайія функціі для виведення списку колег, яких потрібно привітати з днем народження на тижні. 


from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Підготовка Даних
    birthdays = defaultdict(list)
    
    # Отримання Поточної Дати
    today = datetime.today().date()
    
    # Перебір Користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо час народження до типу date
        birthday_this_year = birthday.replace(year=today.year)
        
        # Оцінка Дати на Цей Рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days
        
        # Визначення Дня Тижня
        if 0 <= delta_days < 7:
            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_weekday in ["Saturday", "Sunday"]:
                birthday_weekday = "Monday"  # Якщо це вихідний, переносимо на понеділок
            birthdays[birthday_weekday].append(name)  # Зберігаємо ім'я користувача в відповідний день тижня
    
    # Виведення Результату
    print("Birthdays for next week:")
    for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")  # Виводимо зібрані імена по днях тижня у відповідному форматі   

users = [
    {"name": "Valerii Zaluzhnyi", "birthday": datetime(1973, 7, 8)}, {"name": "Kyrylo Budanov", "birthday": datetime(1986, 1, 4)}, {"name": "Alex Shein", "birthday": datetime(1983, 3, 5)},
]
get_birthdays_per_week(users)