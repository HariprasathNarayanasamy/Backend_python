# To create a dictionary......................

# thisdict={
#     "name":"Hari",
#     "age":21
# }
# print(thisdict)

# accessing dict items...................

# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# print(thisdict["brand"])
# print(thisdict["model"])
# print(thisdict["year"])

# Duplicate is not allowed...................

# thisdict={
#      "brand":"TATA",
#      "model":"nano",
#      "year":2010,
#      "year":2011
# }
# print(thisdict)

# Dictionary length...............


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# print(len(thisdict))

# It can be any data type

# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010,
#     "electric":False
# }
# print(thisdict)


# The Dict constractor

# thisdict=dict(brand="TATA",model="nano",year=2010)
# print(thisdict)


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# x=thisdict.get("model")
# print(x)


# keys() method 


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }

# x=thisdict.keys()
# y=thisdict.values()

# print(x)
# print(y)



# car={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }

# print(car)

# print(type(car))

# car["color"]="white"

# print(car["color"])

# print(car.keys())

# print(car.values())

# print(car)


# Get items in tuple


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }

# print(thisdict.items())


# check if exit.............

# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# if "model" in thisdict:
#     print("True")


# change dict items.............


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# thisdict["year"]=2018
# print(thisdict)


# update dict 


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# thisdict.update({"color":"red"})
# print(thisdict)

# pop() method remove the itmes in specified key name.............


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# thisdict.pop("year")
# print(thisdict)


# del key word....................


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# del thisdict["model"]
# print(thisdict)


# loop dictionary................

# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# for i in thisdict:
#     print(i)




# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# for i in thisdict.values():
#     print(i)



# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# for x,y in thisdict.items():
#     print(x,y)


# to coppy dict............


# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# mydict=thisdict.copy()
# print(mydict)



# thisdict={
#     "brand":"TATA",
#     "model":"nano",
#     "year":2010
# }
# mydict=dict(thisdict)
# print(mydict)


# mydict={
#     "child1":{
#         "name":"cpu",
#         "year":2001
#     },
#     "child2":{
#         "name":"ram",
#         "year":2002
#     },
#     "child3":{
#         "name":"rom",
#         "year":2003
#     }
# }
# print(mydict)
# print(mydict.keys())
# print(mydict.items())
# x=mydict.values()
# print(x)



# child1={
#     "name":"cpu",
#     "year":2001
# }
# child2={
#     "name":"Ram",
#     "year":2002
# }
# child3={
#     "name":"ROM",
#     "year":2003
# }
# mydict={
#     "child1":child1,
#     "child2":child2,
#     "child3":child3
# }

# print(mydict)


# thisdict={
#     "name":"hari",
#     "age":21,
#     "timing":10
# }
# for i in thisdict:
#     print(thisdict[i])


# square_dict={}
# for i in range(1,11):
#     square_dict[i]=i*i

# print(square_dict)

# dict comprehension..................

# square_dict={i:i*i for i in range(1,11)}
# print(square_dict)

# dict1={"key1":1,"key2":2,"key3":3}
# for i in dict1.values():
#     print(i)


# dict1={"key1":1,"key2":2,"key3":3}
# for i in dict1.keys():
#     print(i)


# dict1={"key1":1,"key2":2,"key3":3}
# for (keys,values) in dict1.items():
#     print(keys,values)


# dict1={"key1":1,"key2":2,"key3":3}

# dict2={keys:values*2 for (keys,values) in dict1.items()}  

# print(dict2)
 

# If condition in comprehension....................

# dict1={"hari":20,"vetri":32,"prasath":25,"pradeep":10}

# dict2={k:v for (k,v) in dict1.items() if v%2==0}

# print(dict2)


# mulitiple if condition..............


# dict1={"hari":88,"vetri":32,"prasath":25,"pradeep":10}

# dict2={k: v for (k,v) in dict1.items() if v%2==0 if v<40}

# print(dict2)




# if else coditional dict...............

# dict1={"hari":21,"vijay":45,"pradeep":23,"vetri":20}

# dict2={k:("old" if v>40 else "young") for (k,v) in dict1.items()}

# print(dict2)


# nested dict comprehension..................

# dict1={
#     k1:{k2:k1*k2 for k2 in range(1,6)} for k1 in range(2,5)
# }

# print(dict1)



