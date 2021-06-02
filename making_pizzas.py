from pizza import make_pizza as mp #imports function from module and gives it an alias
import pizza #imports all functions from module
mp(16, 'pepperoni') #calls imported function by alias
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') #calls function from imported module