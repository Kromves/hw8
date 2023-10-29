import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect("homework.db")
cursor = conn.cursor()

while True:
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    print(
        "Вы можете отобразить список сотрудников по выбранному ID города из перечня городов ниже, для выхода введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    # Запрашиваем у пользователя выбор города
    city_id = int(input("Введите ID города: "))

    if city_id == 0:
        break

    # Поиск сотрудников и отображение информации
    cursor.execute("""
            SELECT first_name, last_name
            FROM employees
            WHERE city_id = ?
        """, (city_id,))

    employees = cursor.fetchall()

    if employees:
        print("\nСотрудники в выбранном городе:")
        for employee in employees:
            print(f"{employee[0]} {employee[1]}")
    else:
        print("Сотрудники в этом городе отсутствуют.")

# Закрываем соединение
conn.close()