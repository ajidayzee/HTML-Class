print()
print("Please enter the items of the shopping list (type: quit to finish):")
print()
shopping_cart = []
items = None
print()
while items != "quit":
    items = input("Item: ")

    if items != "quit":
        shopping_cart.append(items)
print("\nThe shopping list is:")
for items in shopping_cart:
    #print(*items, sep='') This code does the same thing as the one below
    print(items)    
print()
print("\nThe shopping list with indexes is:")
for i in range(len(shopping_cart)):
    items = shopping_cart [i]
    print(f"{i}. {items}")
print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_cart[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_cart)):
   item = shopping_cart[i]
   print(f"{i}. {item}")