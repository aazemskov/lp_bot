# https://learn.python.ru/lessons/05_listsanddicts.html?full#12

# Задание 1
## Создайте список из чисел 3, 5, 7, 9 и 10.5
new_list = [3, 5, 7, 9, 10.5]

## Выведите содержимое списка на экран
print(new_list)

## Добавьте в конец списка строку "Python"
new_list.append('Python')

## Выведите длину списка на экран
print(len(new_list))

# Задание 2
## Выведите на экран начальный элемент списка
print(new_list[0])

## Выведите на экран последний элемент списка
print(new_list[-1])

## Напечатайте элементы списка со второго по четвертый включительно
print(new_list[2:5])

## Удалите из списка строку "Python"
new_list.remove('Python')

