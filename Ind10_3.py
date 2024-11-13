def add_two(user_input):
    try:
        num = int(user_input)
        return 2 + num
    except ValueError:
        print("Invalid data type. Expected a number.")
print(add_two("2"))
add_two("string")
add_two("5.23")