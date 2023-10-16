# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

# Access values using keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Update the value associated with a key
my_dict['age'] = 31

# Check if a key exists in the dictionary
if 'name' in my_dict:
    print("Name is in the dictionary.")

# Remove a key-value pair from the dictionary
del my_dict['city']

# Iterate through the keys and values in the dictionary
for key, value in my_dict.items():
    print(key, ":", value)

# Get the number of key-value pairs in the dictionary
num_items = len(my_dict)
print("Number of items in the dictionary:", num_items)
