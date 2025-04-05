#  ЗАДАЧА 2: Проверка на допуск
# 🧠 Условие:
# Ты — система допуска к экзамену.
# Пользователь вводит:
#
# Имя
#
# Возраст
#
# Список предметов, которые он сдал (вводом, через запятую)
#
# 📌 Условия допуска:
#
# Возраст от 18 до 35
#
# В списке сданных предметов обязательно должен быть "математика" (без учёта регистра)
#
# Имя не должно быть пустым
#
# 💡 Пример:

# Введите имя: Денис
# Введите возраст: 27
# Введите сданные предметы (через запятую): математика, физика
# → Вывод: Доступ к экзамену разрешён
#
# Если что-то не так → выводи конкретную причину отказа:
#
# "Доступ запрещён: возраст вне допустимого диапазона"
#
# "Доступ запрещён: отсутствует математика"
#
# "Доступ запрещён: имя не указано"

name = input("Введите имя: ")
age = input("Введите возраст: ")
subjects = input("Введите сданные предметы (через запятую): ")
required_subjects = "математика"

try:
    age = int(age)
except ValueError as error:
    print(f"Ошибка: {error}")
    exit()

if not name or name.isdigit():
    print("Доступ запрещён: имя не указано или указано неверно")
elif age < 18 or age > 35:
    print("Доступ запрещён: возраст вне допустимого диапазона")
elif required_subjects not in subjects.lower():
    print("Доступ запрещён: отсутствует математика")
else:
    print("Доступ к экзамену разрешён")

