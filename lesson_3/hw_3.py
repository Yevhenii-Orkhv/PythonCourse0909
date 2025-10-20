#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

text = ''' alice_in_wonderland = \"Would you tell me, please, which way I ought to go from here?\"
\n"That depends a good deal on where you want to get to," said the Cat.
\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.
\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

print(text)
#-----------------------||-----------------------
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
Total = (Black_sea + Azov_sea) / 2
Comment_for_kids = 'This is just a mathematical example. Nothing more'

print('Black_sea',Black_sea)
print('Azov_sea',Azov_sea)
print('Total_area_of_seas', Total)
print()
print(Comment_for_kids)
print()
print()


 # task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total = 375291
ab = 250449
bc = 222950

C = total - ab
A = total - bc
B = ab - A

print("Перший склад:", A)
print("Другий склад:", B)
print("Третій склад:", C)
print()
print()




# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
per_month_payment = 1179
total_period = 18
full_cost = (total_period * per_month_payment)
print('every month he need to pay', per_month_payment)
print('loan term', total_period)
print ('full PC cost', full_cost)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print()
text = 'остача від діленя чисел'
print(text)

print(8019 % 8)
print(9907 % 9)
print(2789 % 5)
print(7248 % 6)
print(7128 % 5)
print(19224 % 9)
print()

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza = 274
middle_pizza = 218
juce = 35
cake = 350
water = 21

Food = (big_pizza + middle_pizza + cake)
drinks = (juce + water)
total_costs = Food + drinks

print()
print('drinks',drinks)
print('Food', Food)
print('total costs this Birthday party',Food + drinks)
print()




# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
album_page = 6
total_pages = (total_photos / album_page /2)

print()
print("total photos", total_photos)
print('total pages needed', total_pages)
print('rounded number of pages is 20 :)')


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print()
print()
total_range = 1600

gas_cons = 9
car_tank = 48

total_gas = 1600 / 100 * 9
print('total gas for trip', total_gas)
stop_for_gas = total_gas / car_tank
print('stop to charge and enjoy some hot-dogs', stop_for_gas)


