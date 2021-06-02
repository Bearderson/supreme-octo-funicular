def sandwich_items(*toppings):
   """Build a list with all the toppings in it."""
   return toppings


total_toppings = sandwich_items('lettuce', 'mayo', 'pepperoni', 'fingers', 'cheese', 'more cheese', 'forgot more cheese')

print("Your sandwich will be made with these ingredients: \n")
for topping in total_toppings:
    print(f"{topping.title()}")

