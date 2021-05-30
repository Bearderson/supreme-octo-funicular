#store information about a pizza being ordered in a dictionary
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],

}
#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
    