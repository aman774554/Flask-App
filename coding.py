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
