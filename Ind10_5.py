class FutureError(Exception):
    def __init__(self, message="An error occurred!"):
        self.message = message
        super().__init__(self.message)

# Первая функция: деление на ноль
def perform_division(x, y):
    try:
        if y == 0:
            raise FutureError("Error: division by zero!")
        return x / y
    except FutureError as e:
        print(f"Error in perform_division function: {e}")
        return None

# Вторая функция: проверка пустой строки
def validate_string(input_str):
    try:
        if not input_str:
            raise FutureError("Error: empty string!")
        return input_str.upper()
    except FutureError as e:
        print(f"Error in validate_string function: {e}")
        return None

if __name__ == "__main__":
    # Вызов функций
    # Это вызовет ошибку деления на ноль
    result1 = perform_division(10, 0)
    print(result1)
    # Это вызовет ошибку пустой строки
    result2 = validate_string("")
    print(result2)


