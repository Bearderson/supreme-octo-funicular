pets = [
    {'name' : "Snuffles", 'age' : '14', 'type' : 'dog', 'owner' : 'Josh', 'mutations' : 'none'},
    {'name' : "Saber", 'age' : '1', 'type' : 'cat', 'mutations' : 'two tails', 'owner' : 'Losh',},
    {'name' : "Coke", 'age' : '100', 'type' : 'cat', 'mutations' : 'immortality', 'owner' : 'Kosh',},
]

for pet_value in pets:
    print(f"\nName of Pet: {pet_value['name']}")
    print(f"Type of Pet: {pet_value['type']}")
    print(f"Name of Owner: {pet_value['owner']}")
    print(f"Age of Pet: {pet_value['age']}")
    print(f"Mutations: {pet_value['mutations']}")