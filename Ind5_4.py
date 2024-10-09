grades_list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def update_grades(grades):
    return [4 if grade == 3 else grade for grade in grades if grade != 2]

updated_grades1 = update_grades(grades_list1)
updated_grades2 = update_grades(grades_list2)
updated_grades3 = update_grades(grades_list3)

print("Массив 1:", updated_grades1)
print("Массив 2:", updated_grades2)
print("Массив 3:", updated_grades3)
