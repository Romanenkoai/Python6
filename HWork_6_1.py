# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

input_num = list(int(x) for x in input('введите последовательность: ').split())
if input_num == []:
    input_num = [1, 2, 3, 5, 1, 5, 3, 10]

input_num = list(filter(lambda x: input_num.count(x) == 1, input_num ))

print(input_num)
