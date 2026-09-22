# Проект FitLife - MVP версия 1.0

WATER_CONST = 30


print("="*38)
print("Добро пожаловать в наш сервис FitLife!")
print("="*38)                                     


user_name = input("Введите свое имя: ")
user_age = int(input("Введите ваш возраст: "))


# 2. Сбор данных
user_weight = float(input("Введите свой вес в (кг): "))
user_height = float(input("Введите свой рост в (метрах) 'например - 1.70' : "))


def bmi_calculator():
    bmi = user_weight / (user_height**2)
    return bmi


def water_day_norm():
    water_needed = (user_weight * WATER_CONST) / 1000
    return water_needed    


print("="*40)

print(f"\nПривет {user_name}! Ваш результат: ")

print(f"\nПользователь: {user_name}, Возраст - {user_age} ")

print(f"Ваш индекс массы тела(ИМТ): {round(bmi_calculator(),1)}")

print(f"Суточная норма воды: {round(water_day_norm(),1)} л.")

print("\nРасчет окончен. Будьте здоровы!")
