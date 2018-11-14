#list for list and stack
#deque for queue

l = []
for x in range(10):
    l.append(x**2)
print(l)
# it's still exists after the loop completes
print(x)

l = list(map(lambda x: x**2, range(10)))
print(l)
l = [x**2 for x in range(10)]
print(l)
l = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(l)

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)
x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)

s = {1, 6, 5, -2, 3}
print(s)
ss = sorted(s)
print(ss)

d = {x:x**2 for x in s}
print(d)
dd = sorted(d)
print(dd)
print(d.items())
ddd = sorted(d.items(), key = lambda i:i[0])
print(ddd)
