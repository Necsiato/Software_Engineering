
results = [10.2, 14.8, 19.3, 22.7, 12.5,
           33.1, 38.9, 21.6, 26.4, 17.1,
           30.2, 35.7, 16.9, 27.8, 24.5,
           16.3, 18.7, 31.9, 12.9, 37.4]

results.sort()
top_3_best = results[:3]
bottom_3_worst = results[-3:]
starting_from_10th = results[9:]

print("Три лучшие результаты:", top_3_best)
print("Три худшие результаты:", bottom_3_worst)
print("Все результаты начиная с 10-го:", starting_from_10th)
