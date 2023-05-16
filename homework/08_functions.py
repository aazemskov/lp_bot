# Задание 1
## Создайте функцию get_summ(one, two, delimiter='&'),
## которая принимает два параметра, приводит их к строке
## и отдает объединенными через разделитель delimiter
def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'

## Вызовите функцию, передав в нее два аргумента "Learn" и "python",
## положите результат в переменную и выведите ее значение на экран
new_var = get_summ('Learn', 'python')
print(new_var)

## Сделайте так, чтобы результирующая строка выводилась заглавными буквами
new_var = new_var.upper()
print(new_var)

# Задание 2
## Создайте функцию format_price, которая принимает один аргумент price
## Приведите price к целому числу (тип int)
## Верните строку "Цена: ЧИСЛО руб."
## Вызовите функцию, передав на вход 56.24 и положите результат в переменную
## Выведите значение переменной с результатом на экран

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

format_price_result = format_price(56.24)

print(format_price_result)
