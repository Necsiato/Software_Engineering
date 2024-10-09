# Заданные списки
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def form_set(numbers):
    result_set = set()
    for num in set(numbers):
        count = numbers.count(num)
        result_set.add(num)
        for i in range(2, count + 1):
            result_set.add(str(num) * i)
    return result_set

print(form_set(list_1))
print(form_set(list_2))
print(form_set(list_3))