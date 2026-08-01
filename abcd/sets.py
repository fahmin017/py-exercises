# Set:
# ***********

# A set is a collection which is unordered, unchangeable*, and unindexed.

s = {"apple","orange","kiwi"}
print(s)

print("****************************")
s = {"apple","orange","kiwi","apple"} # duplicate ignored
print(s)

print("****************************")

print(len(s)) # 3

print("****************************")

s2 = set(("banana","strawberry","berry")) # set constructor [ set(.......)]
print(s2)

print("****************************")

for i in s:
    print(i)

print("****************************")

print("banana" in s2)
print("banana" not in s2)

print("****************************")

s2.add("passion frt")               # ADD ITEM TO SET
print(s2)

print("****************************")

s2.update(s)
print(s2)

print("****************************")
s2.remove("banana")
print(s2)

print("****************************")

for i in s2:
    print(i)

print("****************************")

s3={1,2,4,9,8}
s4 = s2.union(s3)
print(s4)

print("****************************")

s5=s2.union(s3,s)
print(s5)

print("****************************")

set1 ={1,2,3,4,5}
set2 ={8,9,7,1,6}
set3=set1.intersection(set2)
print(set3)

print("****************************")

set4 = set1.difference(set2)
print(set4)

print("****************************")

set5= set1.symmetric_difference(set2)
print(set5)

print("****************************")

x = frozenset({"apple", "banana", "cherry"})            # FROZENSET
print(x)
print(type(x))

print("****************************")


