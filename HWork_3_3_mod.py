# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list_in = [1.1, 1.2, 3.1, 5, 10.01]

list_in = list(n for n in map(lambda x : x%1, list_in) if n != 0)


# i = 0
# while i < len(list_in):
#     list_in[i] = list_in[i] % 1
#     if list_in[i] == 0: #фильтруем целые так как по условию 0 не является минимумом
#         del list_in[i]
#         continue
#     i+=1

print ('ответ первого варианта: ', max(list_in)-min(list_in))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Do
