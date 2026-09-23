WATER_CONST = 30
DECORATION_EQUAL = 38
CONSTANT_DAILY_NORM = 1000

print("=" * DECORATION_EQUAL)
print("Добро пожаловать в наш сервис FitLife!")
print("=" * DECORATION_EQUAL)

user_name = input("Введите свое имя: ")

while True:
    try:
        user_age = int(
            input("Введите количество полных лет, в целых числах: ")
        )
        break
    except ValueError:
        print("Вы ввели не число!")

user_weight = float(
    input("Введите свой вес в (кг): ")
    .replace(",", ".")
)
user_height = float(
    input("Введите свой рост в (метрах) 'например - 1.70': ")
    .replace(",", ".")
)


def bmi_calculator():
    """Индекс массы тела."""
    return user_weight / (user_height ** 2)


def water_day_norm():
    """Расчет суточной нормы воды."""
    return (user_weight * WATER_CONST) / CONSTANT_DAILY_NORM


print("=" * DECORATION_EQUAL)

print(
    f"Привет {user_name}! Ваш результат: \n"
    f"Пользователь: {user_name}, Возраст - {user_age}\n"
    f"Ваш индекс массы тела(ИМТ): {round(bmi_calculator(), 1)}\n"
    f"Суточная норма воды: {round(water_day_norm(), 1)} л.\n"
    f"Расчет окончен. Будьте здоровы!"
)
