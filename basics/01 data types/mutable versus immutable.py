# immutable: int, float, bool, str, tuple, frozenset

a = 1 
addr1 = id(a)

a += 1
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2)

# mutable: list, set, dict
listData = [0, 1 , 2]
addr1 = id(listData)

listData += [3, 4, 5]
print(listData)

print(addr1)
print(addr2)
print(addr1 == addr2)
