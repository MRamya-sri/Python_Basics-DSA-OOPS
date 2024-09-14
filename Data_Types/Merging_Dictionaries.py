dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)


merged_dict = dict1 | dict2
print(merged_dict)

pop = dict2.pop()
print(pop)

clear = dict1.clear()
print(clear)