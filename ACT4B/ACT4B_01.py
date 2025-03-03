a = {"a", "g", "b", "c", "d", "f"}
b = {"l", "m", "o", "b", "c", "h"}
c = {"k", "i", "j", "h", "c", "d", "f"}

print(len(a.union(b)))
print(len(b - (a | c)))

print("====================================================")
print("i.", c - a)
print("i.", c & a)
print("ii.", (a & b) | (b & c))
print("iii.", (a & c & c) - {'c'})
print("iv.", a & b & c & {'c'})
print("v.", b - (a | c))