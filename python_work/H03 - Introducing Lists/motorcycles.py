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
