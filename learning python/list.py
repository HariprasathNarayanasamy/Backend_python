# access items...............
# x=[2,6,7,4,3,1]
# print(x[0])


# range of index...........
# x=[2,6,7,4,3,1]
# print(x[0:3])

# change list items.........
# x=[2,6,7,4,3,1]
# x[0]=10
# print(x)


# add item to the list...........
# x=[2,6,7,4,3,1]
# x.append(5)
# print(x)


# to insert an item................
# x=[2,6,7,4,3,1]
# x.insert(1,5)
# print(x)


# extend list................
# x=[2,6,7,4,3,1]
# y=[21,22,23,24,25]
# x.extend(y)
# print(x)    


# remove items................
# x=[2,6,7,4,3,1]
# x.remove(6)
# print(x)

# remove items by index no..............
# x=[2,6,7,4,3,1]
# x.pop(0)
# print(x)


# for loop through the list.................
# x=[2,6,7,4,3,1]
# for i in x:
#     print(i)


# while loop through the list.................
# x=[2,6,7,4,3,1]
# i=0
# while i<=(len(x)):
#     print(i)
#     i+=1
    
# clear list items......................

# x=[2,6,7,4,3,1]
# x.clear()
# print(x)

# delete specified item..............
# x=[2,6,7,4,3,1]
# del x[0]
# print(x)

# unpacking list.................
# x=["apple","banana","cherry"]
# [a,b,c]=x
# print(a)
# print(b)
# print(c)

# list comprehension.............

# x=["apple","banana","cherry"]
# [print(x) for x in x]


# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]

# for i in fruits:
#     if "a" in i:
#         newlist.append(i)

# print(newlist)

# names=["hari","ashwin","prasath","pradeep","vetri"]
# newlist=[]

# for i in names:
#     if "a" in i:
#         newlist.append(i)

# print(newlist)

# names=["hari","ashwin","prasath","pradeep","vetri"]

# newlist=[i for i in names if "i" in i and "a" in i ]

# print(newlist)

# print(names)

# names=["hari","ashwin","prasath","pradeep","vetri"]

# newlist=[i for i in names if i!="hari"]

# print(newlist)



# names=["hari","ashwin","prasath","pradeep","vetri"]

# newlist=[i for i  in names ]

# print(newlist)

# newlist=[i for i in range(10)]
# print(newlist)

# newlist=[i for i in range(10) if i<5 and i>0]

# print(newlist)

# names=["hari","ashwin","prasath","pradeep","vetri"]

# newlist=[i.upper() for i in names]

# print(newlist)


# x=["a","b","c"]

# newlist=["hari" for i in x]

# print(newlist)


# names=["hari","ashwin","prasath","pradeep","vetri"]

# names=[i if i!="hari" else "barath" for i in names]

# print(names)



# fruits=["apple","banana","cherry","kiwi"]

# newlist=[i if i!="banana" else "orange" for i in fruits]

# print(newlist)


# 2d list............

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# matrix[0][2]=20
# print(matrix)

# l1=["shoes","coat","shirt","watch"]


# shoes = { 
#     "brand":"jet",
#     "color":"red",
#     "size":21
# }

# coat = {
#     "brand":"get",
#     "color":"red",
#     "size":"L"
# }

# shirt = {
#     "brand":"net",
#     "color":"red",
#     "size":"M"
# }

# watch = {
#     "brand":"fast",
#     "color":"black",
#     "size":"M"
# }

# my_dict = {"shoes": shoes, "coat": coat, "shirt": shirt, "watch": watch}

# print(my_dict)

# l1=["shoes","coat","shirt","pants","watch"]

# l2=[ i for i in l1]
    
# print(l2)



