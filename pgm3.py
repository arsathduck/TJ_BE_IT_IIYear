# IMPLEMENT THE PYTHON ARRAY USING LIST

import array

# Create an array of integers
balance = array.array('i', [100, 200, 300])

# Print the array
print("The array with given values:")
print(balance)

# Accessing an array element at index 2
print("Accessing an array element from index[2]:")
print(balance[2])

# Inserting elements into the array
balance.insert(3, 400)
balance.insert(4, 150)

# Print the array after insertion
print("After Insertion:")
print(balance)

# Accessing the index value of an element (e.g., 400)
print("Accessing the index value of an element (e.g., 400):")
print(balance.index(400))

# Deleting an element from the array (e.g., 150)
balance.remove(150)

# Print the array after deletion
print("After Deleting 150:")
print(balance)

# Traverse the array and print its elements
print("Traverse the array:")
for x in balance:
    print("Array Element:", x)
