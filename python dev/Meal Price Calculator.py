#To show creativity I have added a prompt for price of drinks in line 8
#And also calculated the amount of drinks for all children and adults in line 9 and 10
#Meal prices
child = float(input("What is the price of a child's meal?" + " "))
adult = float(input("What is the price of an adult's meal?" + " "))
no_of_children = int(input("How many children are there?" + " "))
no_of_adults = int(input("How many adults are there?" + " "))
drinks = float(input("What is the price of drinks?" + " "))
drinks_for_children = float(drinks * no_of_children)
drinks_for_adults = float(drinks * no_of_adults)
children_total = float(child * no_of_children+drinks_for_children)
adult_total = float(adult * no_of_adults+drinks_for_adults)
subtotal = float(children_total + adult_total)
print()
print("Subtotal:" + " " + "$" + str(subtotal))
print()
#Sales tax
sales_tax = float(input('What is the sales tax rate?'+" "))
tax = float(subtotal * sales_tax)
sales_tax_rate = float(tax / 100)
print("Sales Tax:" + " " + "$" + str(sales_tax_rate))
total = float(subtotal + sales_tax_rate)
print("Total:"+" "+"$"+str(total))
print()
#Change
payment = float(input("What is the payment amount?"+" "))
change = (payment-total)
print("Change:"+" "+"$"+str(change))