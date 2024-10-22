with open('input.txt', 'a+') as f:
    f.write('\nHow are you, world?')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)