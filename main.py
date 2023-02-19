count = int(input('Введите количество билетов:'))
s = 0
for i in range(count):
    age = int(input('Введите возраст посетителя:'))
    if 18 <= age < 25:
        s += 990
    elif age >= 25:
        s += 1390

if count > 3:
    s = s * 0.9
print('Общая сумма к оплате', s)
