def welcome():
    # Приветствие и сбор данных от клиента
    print("Добро пожаловать в Fit Life!")
    print("=" * 40)


    user_name = input("Ваше имя? ")
    return user_name


def user_data():
    user_age = int(input("Ваш возраст? "))
    weight_kg = float(input("Ваш вес в кг? "))
    height_m = float(input("Ваш рост в метрах, через точку? "))
    return user_age, weight_kg, height_m


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    # Расчёт индекса массы тела уточнил у ИИ
    return weight_kg / (height_m ** 2)


def calculate_water_ml(weight_kg: float) -> float:
    # Расчёт нормы воды в мл уточнил у ИИ
    result = (weight_kg * 30) / 1000
    return result


def main():
    user_name = welcome()
    user_age, weight_kg, height_m = user_data


    bmi_result = calculate_bmi(weight_kg, height_m)
    needed_water = calculate_water_ml(weight_kg)


    print("=" * 40)
    print("Данные гостя:")
    print("=" * 40)
    print(f"Имя: {user_name}")
    print(f"Возраст: {user_age} лет")
    print(f"Вес: {weight_kg} кг")
    print(f"Рост: {height_m} м")
    print(f"ИМТ: {bmi_result:.1f}")
    print(f"Норма воды: {needed_water} мл в день")


if __name__ == "__main__":
    main()
