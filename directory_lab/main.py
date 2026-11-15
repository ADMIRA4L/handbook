
# Лабораторная работа №4
# Работа со структурами данных и файлами
# Приложение "Справочник"

import os

# Словарь: имя -> кортеж с данными
directory = {}


# Загрузка данных из файла
def load_data():
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')

                if len(parts) == 4:
                    name, phone, email, city = parts
                    directory[name] = (phone, email, city)

        print("Данные успешно загружены.")

    except FileNotFoundError:
        print("Файл data.txt не найден. Будет создан новый справочник.")


# Сохранение данных в файл
def save_data():
    with open('data.txt', 'w', encoding='utf-8') as f:
        for name, data in directory.items():
            f.write(f"{name}|{data[0]}|{data[1]}|{data[2]}\n")


# Добавление контакта
def add_contact():
    name = input("Введите имя: ")

    if name in directory:
        print("Такой контакт уже существует!")
        return

    phone = input("Введите номер телефона: ")
    email = input("Введите электронную почту: ")
    city = input("Введите город: ")

    directory[name] = (phone, email, city)

    save_data()
    print("Контакт успешно добавлен!")


# Поиск контакта
def search_contact():
    name = input("Введите имя для поиска: ")

    if name in directory:
        data = directory[name]

        print("\nКонтакт найден:")
        print("Имя:", name)
        print("Телефон:", data[0])
        print("Email:", data[1])
        print("Город:", data[2])
    else:
        print("Контакт не найден.")


# Вывод всех контактов
def show_contacts():
    if not directory:
        print("Справочник пуст.")
        return

    print("\n========== СПИСОК КОНТАКТОВ ==========")

    for name, data in directory.items():
        print(f"\nИмя: {name}")
        print(f"Телефон: {data[0]}")
        print(f"Email: {data[1]}")
        print(f"Город: {data[2]}")

    print("\n======================================")


# Удаление контакта
def delete_contact():
    name = input("Введите имя контакта для удаления: ")

    if name in directory:
        del directory[name]
        save_data()
        print("Контакт удалён.")
    else:
        print("Контакт не найден.")


# Главное меню
def main():
    load_data()

    while True:
        print("\n========== СПРАВОЧНИК ==========")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Показать все контакты")
        print("4. Удалить контакт")
        print("5. Сохранить данные")
        print("0. Выход")
        print("================================")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            show_contacts()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            save_data()
            print("Данные сохранены.")

        elif choice == "0":
            save_data()
            print("Работа программы завершена.")
            break

        else:
            print("Неверный пункт меню. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
