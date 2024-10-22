def calculate_revenue():
    total_revenue = 0
    with open('ind5_input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            product, quantity, price = line.strip().split(', ')
            quantity = int(quantity)
            price = float(price)
            revenue = quantity * price
            total_revenue += revenue
    return total_revenue
revenue = calculate_revenue()
print(f'Выручка: {revenue}')
