abcd = {
    'name' : 'fahmin',
    'age' : '21'
}
print(abcd)
# print(abcd.clear())

abcd.update({'place':'calicut'})
print(abcd)

abcd.pop('place')
print(abcd)

abcd.update({"city": "kkd"})
print(abcd)

del abcd["city"]
print(abcd)