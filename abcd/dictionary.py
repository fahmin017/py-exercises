# abcd = {
#     'name' : 'fahmin',
#     'age' : '21'
# }
# print(abcd)
# # print(abcd.clear())

# abcd.update({'place':'calicut'})
# print(abcd)

# abcd.pop('place')
# print(abcd)

# abcd.update({"city": "kkd"})
# print(abcd)

# del abcd["city"]
# print(abcd)

d={
    "name":"fahmin",
    "age":22,
    "place":"kinalur"
}
print(d)

print("****************************")

print(d["place"])

print("****************************")

print(len(d))

print("****************************")

d2 = dict(name ="messi",age=39,place="rosario")
print(d2)

print("****************************")

a=d.get("name")
print(a)

print("****************************")

x=d.keys()
print(x)

print("****************************")

d["name"]="finu"            # CHANGE VAULES
print(d)

print("****************************")

y=d.values()
print(y)

print("****************************")

d["id"]=122
print(d)

print("****************************")

d.update({"name":"fahmin"})
print(d)

print("****************************")

d.pop("id")
print(d)

print("****************************")

for x in d:
    print(x)

print("****************************")

for i in d:
    print(d[i])

print("****************************")

my_fam ={
    "child1":{
        "name":"finu",
        "age":22
    },

    "child2":{
        "name":"sanu",
        "age":18
    },
    "child3":{
        "name":"radhin",
        "age":14
    },
    "child4":{
        "name":"emin",
        "age":7
    }
}
print(my_fam)
a=my_fam.keys()
print(a)
b=my_fam.values()
print(b)

print("****************************")

print(my_fam["child1"]["name"])

print("****************************")

for x, obj in my_fam.items():
    print(x)
    for y in obj:
        print(y,":",obj[y])

print("****************************")
