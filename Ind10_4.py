import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        #время начала выполнения
        start_time = time.time()
        #оригинальную функцию
        result = func(*args, **kwargs)
        #время окончания выполнения
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of function '{func.__name__}': {execution_time:.5f} seconds")
        return result
    return wrapper

# Функция для вычисления факториала
@log_execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Функция для вычисления суммы квадратов чисел от 1 до n
@log_execution_time
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def measure_execution_time(func):
    start_time = time.time()  # Засекаем время начала
    func()  # Выполняем функцию
    end_time = time.time()  # Засекаем время конца
    execution_time = end_time - start_time  # Разница времени

    print(f"Execution time: {execution_time:.5f} seconds")
# Вызов функций для проверки работы
factorial_result = factorial(100)
print(f"Factorial: {factorial_result}")

sum_of_squares_result = sum_of_squares(100)
print(f"Sum of squares from 1 to 10: {sum_of_squares_result}")
