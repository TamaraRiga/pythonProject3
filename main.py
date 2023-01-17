# ЗАДАНИЕ 13.8.19 (HW-03)
person = int(input('Введите необходимое количество билетов: '))
price = 0
for t in range(1, person + 1):
    age = int(input(f'Введите возраст посетителя № {t}: '))
    if age < 18:
        price += 0
        print('Билет бесплатный')
    elif 18 <= age < 25:
        price += 990
        print('Стоимость билета 990 руб.')
    else:
        price += 1390
        print('Стоимость билета 1390 руб.')
print('Общая стоимость %d билетов: ' %(person), price, 'руб.')
if person > 3:
    price = price - ((price / 100) * 10)
    print('Вы получаете дополнительную скидку 10% за покупку более 3-х билетов')
    print('Общая стоимость %d билетов c учетом всех скидок:' %(person), int(price), 'руб.')