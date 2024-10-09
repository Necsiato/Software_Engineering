import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

a_max = max(one)
b_max = max(two)
c_max = max(three)

a_min = min(one)
b_min = min(two)
c_min = min(three)

def heron_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

area_max = heron_area(a_max, b_max, c_max)
area_min = heron_area(a_min, b_min, c_min)

print("Максимальные стороны:", area_max)
print("Минимальные стороны:", area_min)
