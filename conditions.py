user_age = input("Введите свой возраст: ")

if not user_age.isdigit():
    print("Ввод должен быть исклячительно числом!")
elif 18 <= int(user_age) <= 60:
    print("Добро пожаловать!")
elif int(user_age) > 60:
    print("Рекомендуем отдых, но доступ открыт")
else:
    print("Доступ запрещён")