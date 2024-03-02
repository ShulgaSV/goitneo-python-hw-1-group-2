    #Консольний бот помічник, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.



def parse_input(user_input):  # Функція для розбору введеного користувачем рядка
    cmd, *args = user_input.split()  # Розбиває введений рядок на слова
    cmd = cmd.strip().lower()  # Видаляє зайві пробіли та переводить команду до нижнього регістру
    return cmd, *args

def add_contact(args, contacts):  # Функція для додавання нового контакту
    name, phone = args  # Розпаковка аргументів
    contacts[name] = phone  # Додавання контакту до словника
    return "Contact added."  # Повідомлення про успішне додавання

def change_contact(args, contacts):  # Функція для зміни контакту
    name, phone = args  # Розпаковка аргументів
    if name in contacts:  # Перевірка чи існує контакт з таким ім'ям
        contacts[name] = phone  # Зміна номера телефону для вказаного контакту
        return "Contact updated."  # Повідомлення про успішну зміну контакту
    else:
        return "Contact not found."  # Повідомлення про невдачу, якщо контакт не знайдено

def show_all(contacts):  # Функція для виведення усіх контактів
    if contacts:  # Перевірка чи існують контакти
        for name, phone in contacts.items():  # Прохід по усіх парам ключ-значення у словнику контактів
            print(f"{name}: {phone}")  # Виведення ім'я та номера телефону контакту
    else:
        print("No contacts found.")  # Повідомлення про відсутність контактів, якщо словник пустий

def main():  # Основна функція програми
    contacts = {}  # Ініціалізація словника контактів
    print("Welcome to the assistant bot!")  # Виведення привітання
    while True:  # Безкінечний цикл для введення команд користувачем
        user_input = input("Enter a command: ")  # Зчитування команди від користувача
        command, *args = parse_input(user_input)  # Розбір команди на окремі частини

        if command in ["close", "exit"]:  # Перевірка чи команда для завершення програми
            print("Good bye!")  # Виведення повідомлення про завершення роботи
            break  # Вихід з циклу
        elif command == "hello":  # Перевірка чи команда для виведення привітання
            print("How can I help you?")  # Виведення привітання
        elif command == "add":  # Перевірка чи команда для додавання контакту
            print(add_contact(args, contacts))  # Виклик функції для додавання контакту
        elif command == "change":  # Перевірка чи команда для зміни контакту
            print(change_contact(args, contacts))  # Виклик функції для зміни контакту
        elif command == "all":  # Перевірка чи команда для виведення усіх контактів
            show_all(contacts)  # Виклик функції для виведення усіх контактів
        else:
            print("Invalid command.")  # Повідомлення про невірну команду

if __name__ == "__main__":  # Перевірка чи код виконується як самостійна програма
    main()  # Виклик основної функції програми