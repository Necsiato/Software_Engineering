def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'

        return input_func(name, age)

    return output_func


@check
def personal_info(name, age):
    print(f"Имя: {name}, Возраст: {age}")


if __name__ == '__main__':
    personal_info('Владимир', 38)
    personal_info('Вадим', -5)
    personal_info('Мария', 138, 15, 48, 2)