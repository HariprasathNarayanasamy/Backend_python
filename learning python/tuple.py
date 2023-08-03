# x=("a","b","c")
# print(type(x))


# change tuple values.............

# tuple1=("a","b","c")
# x=list(tuple1)
# x[2]="d"
# tuple1=tuple(x)
# print(tuple1)

# add items.....................

# x=("a","b","c")
# y=list(x)
# y.append("d")
# x=tuple(y)
# print(x)


# add tuple to a tuple...............

# x=("a","b","c")
# y=("d",)
# x+=y
# print(x)

# unpacking tuple.................

# fruits=("apple","banana","cherry")
# (green,yellow,red)=fruits
# print(green)
# print(yellow)
# print(red)

# fruits=("apple","banana","cherry")
# for i in fruits:
#     print(i)


# fruits=("apple","banana","cherry","strawberry","raspberry")
# (green,yellow,*red)=fruits
# print(green)
# print(yellow)
# print(red)

# loop through the index no and len..................

# fruits=("apple","banana","cherry")
# for i in range(len(fruits)):
#     print(fruits[i])

# while loop...................

# fruits=("apple","banana","cherry")
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# count method.................

# tuple1=('a','b','a','d')
# x=tuple1.count("a")
# print(x)

# index method..................

# x=("a","b",'c','d')
# print(x.index("b"))


# x=("a","b","c","a")
# y=x*2
# print(y)
# print(y.index("b"))

# print(type(y))