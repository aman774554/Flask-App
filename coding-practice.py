https://chatgpt.com/share/67e4e94d-9bac-800d-af88-d9e2eda8b360
# Dictionary
dict1 = {"a":1,"b":3,"c":2}
dict2 = {"b":4,"d":5,"a":30}

dict1.update(dict2)
print(list(d.keys()))  # ['a', 'b', 'c']
print(list(d.values()))  # [1, 2, 3]
print(dict((sorted(dict1.items(), key=lambda x: x[1])))) # Sort a dictionary by values
print({v:k for k,v in dict1.items()}) #swap keys and values
print("d" in dict1) # key exists in a dictionary True
print(max(dict1, key=dict1.get)) # maximum value in a dictionary
print({k:v for k,v in dict1.items() if v>25})
print({k:v for k,v in dict1.items() if k not in "abc"})
print(sum(dict1.values()))
================================================
# string
str1 = "naman"
s1, s2 = "listen", "silent"
str2 = "aman chaturvedi"

print(str1[::-1])
print(str1 == str1[::-1])
print(str1.count("a"))
print(str1.replace('n','zzz'))
print(s.find("world"))  # 6
print(s.title())  # "Hello World"
print(s.isdigit())  # True
print(str1.upper())
print(str1.lower())
print(sorted(s1)==sorted(s2))
print(max(s.split(), key=len))  # "amazing"
print(''.join([char for char in str1 if char.lower() not in  'aeiou']))
print(len(s1) == len(s2) and s2 in s1) 
print(" ".join(s.split()[::-1]))  # "World Hello"
================================================
#List
lst = [1,4,5,3,2,5,8]

print(lst[::-1])
print(max(lst), min(lst))
print(sorted(lst))
print(sorted(lst, reverse=True))
print(list(set(lst)))
print(lst.index(5))
from collections import Counter
lst2 = [1, 2, 3, 1, 2, 1]
mydict = dict(Counter(lst2))
print(max(mydict, key=mydict.get)) #Max dict value
lst3 = [[1, 2], [3, 4], [5]]
print([item for sublist in lst3 for item in sublist]) # Flat
print(sorted(set(lst))[-2])  # 2nd largest
print(lst[k:]+lst[:k]) # Rotate by k
print(list(set(lst1) & set(lst2)))  # Intersection
print(list(set(lst1) | set(lst2)))  # Union
print(list(set([val for val in lst2 if lst2.count(val) > 1]))) # Duplicate
print(list(set(range(min(lst), max(lst) + 1)) - set(lst))) #missing nums
print([sum(lst[:i+1]) for i in range(len(lst))])  # commulative sum # [1, 3, 6, 10]

