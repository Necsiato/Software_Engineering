def add_expense():
    expense_info = input("Инфорамция о расходах - ")
    expense_count = input("Сумма расходов - ")
    with open('ind2_input.txt', 'a', encoding='utf-8') as f:
        f.write(f'{expense_info} = {expense_count}\n')

def input_expense():
    with open('ind2_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip(' '))

while True:
    user_command = input('1 - add, \n2 - show \n')
    if user_command == '1':
        add_expense()
    elif user_command == '2':
        input_expense()
    else:
        print('error')
