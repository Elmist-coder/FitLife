#Приветствие клиента
#знакомство с клиентом
print(f"Добро Пожаловать в Fit Life!")
print("=" * 40)
#Уточнение данных о клиенте
user_name = input("Ваше имя?: ")
user_age = int(input("Ваш возраст?: "))
weight_kg = float(input("Ваш вес в кг: "))
height_m = float(input("Ваш рост в метрах, через точку: "))
print("=" * 40)
#расчитываем индекс массы тела
import math as mt
bmi = weight_kg / (height_m ** 2)

#расчитываем необходимое количество жидкости в мл
water_ml = weight_kg * 30 
print(f"Подведём итог:")
print(f'Ваше имя: {user_name}')
print(f'Ваш возраст: {user_age}', "г")
print(f'Ваш вес: {weight_kg}', "кг")
print(f'Ваш рост: {height_m}', "м")
print(f"Ваш ИМТ:", int (bmi))
print(f"Ваша норма воды:, {water_ml:.1f} мл. в день")

print("Расчет окончен. Будьте здоровы!")