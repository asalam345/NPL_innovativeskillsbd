words = ["hi", "python", "is", "cool", "code", "a"]
isGreaterThan3 = lambda w: len(w) > 3
newList = [w for w in words if isGreaterThan3(w)]

print(newList)