# https://learn.python.ru/lessons/05_listsanddicts.html?full#14

# Задание 1
## Создайте словарь:
## {"city": "Москва", "temperature": "20"}
info_dict = {
    'city': 'Москва',
    'temperature': '20'
    }

## Выведите на экран значение ключа city
print(info_dict.get('city'))

## Уменьшите значение "temperature" на 5
info_dict['temperature'] = str(int(info_dict['temperature']) - 5)

## Выведите на экран весь словарь
print(info_dict)

# Задание 2
## Проверьте, есть ли в словаре ключ country
print(info_dict.get('country'))

## Выведите значение по-умолчанию "Россия" для ключа country
print(info_dict.get('country', 'Россия'))

## Добавьте в словарь элемент date со значением "27.05.2019"
info_dict['date'] = '27.05.2019'

## Выведите на экран длину словаря
len(info_dict)

