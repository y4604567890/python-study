print("\nList test:")
l = [0, 1, 1, 2, 3, 5, 8, 13, 21]
l.append(13 + 21)
print(l)
print(len(l))
print(l[5:9])
# It's copy from l, not point to l.
l2 = l[5:9]
m = l2
# ll change, but l not.
m[0] = 111
print(m)
print(l2)
print(l)

#copy l to l3
l3 = l[:]
l3[5:9] = [100]
print(l)
print(l3)
l3[:] = []
print(l3)

a = [l2, l3]
print(a)
if (a):
    print("a is not null")
