# Modifying Elements in a list

# List of motorcycles, return value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modify first value to be ducati instead of honda
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding (append) item to the back of the list
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Assigning (insert) item to spot inside list
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print (motorcycles)

# Removing (del) item from list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles [0]
print(motorcycles)

# Removing (pop) item from list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# popped_motorcycle = popped item (last item in list)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# popping items from any position in a list (give pop() an index number)
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Removing an assigned value + reason
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

