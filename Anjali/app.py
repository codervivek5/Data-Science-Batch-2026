# List comprehension

# mylist = [expession for item in iterable if condition]

# num = [x for x in range(1,10)]
# print(num)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# x = thisdict.items()

# # x = thisdict.keys()
# # thisdict["size"] = "Economy"
# # x = thisdict.get("brand")
# print(x)


for i in thisdict.values():
    print(i)
    # print(i ,"=" ,thisdict[i])