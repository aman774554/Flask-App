# Dictionary
dict1 = {"a":1,"b":3,"c":2}
dict2 = {"b":4,"d":5,"a":30}

dict1.update(dict2)
print(dict1)
print(dict((sorted(dict1.items(), key=lambda x: x[1]))))
print({v:k for k,v in dict1.items()})
print("d" in dict1)
print(max(dict1, key=dict1.get))
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
print(str1.upper())
print(str1.lower())
print(sorted(s1)==sorted(s2))
print(''.join([char for char in str1 if char.lower() not in  'aeiou']))
print(len(s1) == len(s2) and s2 in s1) 
print(' '.join((str2.split(" ")[::-1])))
================================================
#List

