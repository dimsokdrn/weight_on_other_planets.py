# weight_on_other_planets.py

# Ввод данных от пользователя
weight_earth = float(input("Введите ваш вес на Земле (в килограммах): "))

# Коэффициенты для расчета веса на других планетах
gravity_factor = {
    "Меркурий": 0.38,
    "Венера": 0.91,
    "Марс": 0.38,
    "Юпитер": 2.34,
    "Сатурн": 1.06,
    "Уран": 0.92,
    "Нептун": 1.19
}

# Расчет веса на других планетах
print("Вес на других планетах:")
for planet, factor in gravity_factor.items():
    weight_other_planet = weight_earth * factor
    print("- {} : {:.2f} кг".format(planet, weight_other_planet))
