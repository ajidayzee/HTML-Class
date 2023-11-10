#Welcome display and menu
print('Welcome to the Shopping Cart Program!')
print('Please select one of the following:')
print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
print()
choice = int(input('Please enter an action:  '))

# creating lists and empty variables
shopping_cart = [ ]
quantity = [ ]
prices = [ ]
item = None
qty = ' '
cost = None

# loop for choice 1
while choice != 2 and choice != 3 and choice != 4 and choice != 5:
    item = input('What item would you like to add?  ')
    qty = int(input('What is the quantity?  '))
    cost = float(input(f"What is the price of '{item}'?  "))
    total_cost = cost * qty
    print(f"'{item}' has been added to the cart.")
    if choice != 2 and choice != 3 and choice != 4 and choice != 5:
        shopping_cart.append(item)
        quantity.append(qty)
        prices.append(total_cost)
    
    print()

    print('Please select one of the following:')
    print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
    choice = int(input('Please enter an action:  '))
print()

#loop for choice 2
while choice != 1 and choice != 3 and choice != 4 and choice != 5:
    print('The contents of the shopping cart are:')
    print('\tItem \t\tQuantity \tPrice\n')

    for i in range (len(shopping_cart)):
        items = shopping_cart[i]
        item_qty = quantity[i]
        cost_price = prices[i]
        print(f'{i + 1}.\t{items}\t \t{item_qty}\t \t${cost_price:3}')

    print()

    print('Please select one of the following:')
    print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
    choice = int(input('Please enter an action:  '))


print()

#loop for choice 5
while choice != 1 and choice != 2 and choice != 3 and choice != 4:
    if choice != 1 and choice != 2 and choice != 3 and choice != 4:
        break
print('Thank you. Goodbye')