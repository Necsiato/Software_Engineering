def median(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

if __name__ == '__main__':
    result = median(1,2,3,4,5,6,7,8,9,10)
    print(f"Среднее арифметическое = {result}")