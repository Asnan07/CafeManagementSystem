print("\n Welcome to Kawaii Cafe :) \n\n")

menu = {
    "Espresso": 2,
    "Iced Tea": 2.75,
    "Latte":3.0,
    "Cappuccino":3.50,
    "Cookies": 1.50,
    "Donuts": 1.50,
    "Croissants":2.50,
    "Muffins": 2.00,
    "Brownies": 2.00,
    "Americano": 5.00
    }
bill = 0
bill_detail = {}

for i in menu:
    print(i.ljust(20),"-",menu[i])

while True:
  order = input("Please enter the items you would like to order OR enter DONE to exit: ")
  if order == "DONE":
      break
  
  elif order in menu:
      quantity = int(input("Enter the Quantity: "))
      bill_detail[order] = quantity

  else:
      print("Please enter valid item name.")

for item in bill_detail:
  item_cost = bill_detail[item]*menu[item]
  bill = bill + item_cost
  print(f"{item.ljust(10)}\t{bill_detail[item]}\t{item_cost}")

print("\nYour bill is",bill,"$")