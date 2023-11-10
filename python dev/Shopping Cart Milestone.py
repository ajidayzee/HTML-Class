#Shopping Cart Milestone
#Welcome display and menu
print('Welcome to the Shopping Cart Program!')
print('Please select one of the following:')
print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
print()
choice = int(input('Please enter an action:  '))
print()
shopping_cart = []
items = None
all_prices = []
prices = None
while items != "quit" and prices != "quit":
    items = input("What item would you like to add? ")
    prices = (input("What is the price of" + " " + "'" + items + "'" +"? "))
    print("'" +items + "'" + "has been added to the cart.")
    print()

    if items != "quit" and prices != "quit":  
        shopping_cart.append(items)
        all_prices.append(prices)
    elif items != "quit" or prices != "quit":
        shopping_cart.append(items)
        all_prices.append(prices)
    else:   
        print("\nThe contents of the shopping cart are:")
print()
for i in range(len(shopping_cart)):
    items = shopping_cart [i]
    prices = all_prices [i]
    print(f"\n{i + 1}. {items}" , end='') 
    print(f" - ${prices}", end='')   