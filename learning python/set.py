# set...............
# thisset={"apple","banana","cherry"}
# print(thisset)



# thisset=set(("apple","banana","cherry"))
# print(type(thisset))
# print(thisset)

# thisset={"apple","banana","cherry","apple"}
# print(thisset)

# get the length of the set................

# thisset={"apple","banana","cherry"}
# print(len(thisset))


# set1={"abc",34,True,"hari"}
# print(set1)

# for loop in set......................

# myset={"apple","banana","cherry"}
# for i in myset:
#     print(i)

# to check the item present are not...................

# myset=set(("apple","banana","cherry"))
# print("banana" in myset)


# To add new items........................

# x={"a","b","c"}
# x.add("d")
# print(x)

# To add a new set to existing set

# x={"a","b","c","d"}
# y={1,2,3,4,5,6}
# x.update(y)
# print(x)


# to remove set items

# x={"x","y","z"}
# x.remove("x")
# print(x)


# x={"x","y","z"}
# x.discard("y")
# print(x)


# loop through sets

# x={"a","b","c"}
# for i in x:
#     print(i)


# To join two sets

# x={"a","b","c"}
# y={1,2,3}
# print(x.union(y))


# x={"a","b","c"}
# y={1,2,3}
# x.update(y)
# print(x)


# Keep only the duplicates

# x={"a","b","c"}
# y={"a","d","e"}
# x.intersection_update(y)
# print(x)


# x={"a","b","c"}
# y={"a","d","e"}
# z=x.intersection(y)
# print(z)

# Keep all but not the duplicates

# x={"a","b","c"}
# y={"d","e","a"}
# x.symmetric_difference_update(y)
# print(x)



##################### assingments on sets ######################


#1. Write a Python program to create a set..........

# print("empty set")
# x=set()
# print(x)
# print(type(x))
# print("non empty set")
# x=set(("a","b","c"))
# print(x)



# 2. Write a Python program to iteration over sets......


# x={"a","b","c"}
# for i in x:
#     print(i)



# 3. Write a Python program to add member(s) in a set.

# x={"a","b","c"}
# x.add("s")
# print(x)


# 4. Write a Python program to remove item(s) from a given set.

# x={"a","b","c","s"}
# x.remove("s")
# print(x)

# 5. Write a Python program to remove an item from a set if it is present in the set.

# x={"a","b","c"}
# y={"d","e","a"}
# x.symmetric_difference_update(y)
# print(x)

# 6. Write a Python program to create an intersection of sets.

# x={"a","b","c"}
# y={"d","e","a","c"}
# x.intersection_update(y)
# print(x)

# 7. Write a Python program to create a union of sets.

# x={"a","b","c"}
# y={1,2,3}
# z=x.union(y)
# print(z)

# 8. Write a Python program to create set difference

# x={"a","b","c"}
# y={"d","e","a"}
# x.symmetric_difference_update(y)
# print(x)
