## List
A list is an ordered, mutable collection that allows duplicate elements.

```python
# Creating a list
my_list = [1, 2, 3, 4, 5, 2]

# 1. append() - Adds an item to the end of the list
my_list.append(6)
print(my_list)  # [1, 2, 3, 4, 5, 2, 6]

# 2. extend() - Adds multiple elements at the end
my_list.extend([7, 8])
print(my_list)  # [1, 2, 3, 4, 5, 2, 6, 7, 8]

# 3. insert() - Inserts an element at a specific index
my_list.insert(2, 99)
print(my_list)  # [1, 2, 99, 3, 4, 5, 2, 6, 7, 8]

# 4. remove() - Removes first occurrence of a value
my_list.remove(2)
print(my_list)  # [1, 99, 3, 4, 5, 2, 6, 7, 8]

# 5. pop() - Removes and returns an element at a given index (default: last)
removed = my_list.pop()
print(removed)  # 8
print(my_list)  # [1, 99, 3, 4, 5, 2, 6, 7]

# 6. index() - Returns the first index of a given value
index = my_list.index(99)
print(index)  # 1

# 7. count() - Counts occurrences of a value
count = my_list.count(2)
print(count)  # 1

# 8. sort() - Sorts the list in ascending order
my_list.sort()
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 99]

# 9. reverse() - Reverses the list order
my_list.reverse()
print(my_list)  # [99, 7, 6, 5, 4, 3, 2, 1]

# 10. copy() - Returns a shallow copy
copy_list = my_list.copy()
print(copy_list)  # [99, 7, 6, 5, 4, 3, 2, 1]

# 11. clear() - Removes all elements
my_list.clear()
print(my_list)  # []
```
## Tuple
A tuple is an ordered, immutable collection that allows duplicate elements.
```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5, 2)

# 1. count() - Counts occurrences of a value
print(my_tuple.count(2))  # 2

# 2. index() - Returns the first index of a value
print(my_tuple.index(4))  # 3

# Tuples are immutable, but we can concatenate them
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # (1, 2, 3, 4, 5, 2, 6, 7)
```
## Set
A set is an unordered, mutable collection that does not allow duplicate elements.
```python
# Creating a set
my_set = {1, 2, 3, 4, 5}

# 1. add() - Adds an element to the set
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# 2. remove() - Removes an element (raises error if not found)
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5, 6}

# 3. discard() - Removes an element (no error if not found)
my_set.discard(10)  # No error

# 4. pop() - Removes a random element
removed_element = my_set.pop()
print(removed_element)  # Random element
print(my_set)

# 5. clear() - Removes all elements
my_set.clear()
print(my_set)  # set()

# Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

# 6. union() - Combines sets
print(A.union(B))  # {1, 2, 3, 4, 5}

# 7. intersection() - Common elements
print(A.intersection(B))  # {3}

# 8. difference() - Elements in A but not in B
print(A.difference(B))  # {1, 2}

# 9. symmetric_difference() - Elements in A or B, but not both
print(A.symmetric_difference(B))  # {1, 2, 4, 5}
```
## Dictionary
A dictionary is an unordered collection of key-value pairs.
```python
# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 1. get() - Gets value by key (returns None if key not found)
print(my_dict.get("name"))  # Alice
print(my_dict.get("country", "Not Found"))  # Not Found

# 2. keys() - Returns all keys
print(my_dict.keys())  # dict_keys(['name', 'age', 'city'])

# 3. values() - Returns all values
print(my_dict.values())  # dict_values(['Alice', 25, 'New York'])

# 4. items() - Returns key-value pairs
print(my_dict.items())  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# 5. update() - Updates dictionary with another dictionary
my_dict.update({"age": 26, "country": "USA"})
print(my_dict)  # {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# 6. pop() - Removes a key and returns its value
age = my_dict.pop("age")
print(age)  # 26
print(my_dict)  # {'name': 'Alice', 'city': 'New York', 'country': 'USA'}

# 7. popitem() - Removes the last inserted key-value pair
last_item = my_dict.popitem()
print(last_item)  # ('country', 'USA')
print(my_dict)  # {'name': 'Alice', 'city': 'New York'}

# 8. clear() - Removes all elements
my_dict.clear()
print(my_dict)  # {}

# 9. fromkeys() - Creates a dictionary with given keys and default value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}
```

