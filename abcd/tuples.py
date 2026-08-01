# tuple=(1,2,3,4,5,6)
# print(tuple)
# print(sum(tuple))
# print(len(tuple))
# print(min(tuple))
# print(max(tuple))

# print(tuple[1])

# print(tuple.count(5))

# abcd=("hari","kichu","acadeno")
# print(abcd)

# print(abcd[2])

# abc = list(abcd)
# print(abc)

# abc.append("sam")
# print(abc)

# wh = tuple(abc)
# print(wh)

tup=("apple",)
print(type(tup))

tup1=("apple",34,True)
print(type(tup1))

tup2=(2,5,8,4,2,12,7,2,5)
print(tup2[:3])

print(tup2[-1])

if 12 in tup2:
    print("present")

list1 = list(tup2)
list1[0]= 10                            # UPDATING A TUPLE
tup2 = tuple(list1)                     # COVETING TO A LIST - UPDATE - BACK TO TUPLE
print(tup2)


a=list(tup2)
a.append(5)
tup2=tuple(a)
print(tup2)


tup2 = tup2+tup1
print(tup2)

t = ("barca","real","city")
(red,white,blue) = t
print(red)
print(blue)
print(white)

clubs = ("barca","real","city","united","milan")
(red,white,*blue) = t
print(red)
print(blue)
print(white)

print("*************************")

for i in clubs:
    print(i)

print("*************************")

for i in range(len(clubs)):
    print([i])

print("*************************")

tup4=tup1+clubs
print(tup4)