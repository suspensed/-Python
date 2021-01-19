profit = int(input('Введите прибыль компании: '))
lesion = int(input('Введите убытки компании: '))

if profit > lesion:
	proceeds = profit - lesion
	print(f'Ваша компания работает в плюс. Рентабельность компании {proceeds} рублей')
	staff = int(input('Сколько в вашей компании, работает людей? '))
	print(f'Доход одного вашего сотрудника составляет {round(proceeds / staff)} рублей ')
else:
	print('Ваша компания работает в убыток')