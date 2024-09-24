counter = 0
string = 'hello'
memory = 'world'
values = [0,2,4,6,8,10]
while counter != 10:
    if counter in values:
        print(string + ' world')
        memory = string
        string = memory
        print(memory)

    counter+=1

if counter>7:
    string = 'world'
    print(memory, string)


