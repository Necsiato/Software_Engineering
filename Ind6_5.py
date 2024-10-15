def cumulative_sum(lst):
    result = []
    current_sum = 0
    for num in lst:
        current_sum += num
        result.append(current_sum)
    return result

print(cumulative_sum([1, 2, 3, 4]))
print(cumulative_sum([5, 10, 15]))
print(cumulative_sum([3, -2, 7, 4, -1]))