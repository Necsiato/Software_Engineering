user_input = input()

def analyze_digits(number_str):
    count_dict = {}
    for symbol in number_str:
        num = int(symbol)
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    return dict(sorted_count[:3])

print(analyze_digits(user_input))
