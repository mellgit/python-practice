"""
В any и all можно передавать только коллекции.
Если передавать только какие-то конкретные значения переменных,
то их необходимо обернуть в список или кортеж, иначе
выпадает ошибка
"""
arr = ['hello','world','hi'] 
print(any(arr)) # если хотя бы ОДИН элемент НЕ пустой
print(all(arr)) # если ВСЕ элементы НЕ пустые

a = 123
b = 'asdf'

print(all([a, b]))
print(any((a, b)))