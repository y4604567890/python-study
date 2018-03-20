def f(a, L=[]):
    L.append(a)
    return L

print(f(100, [-1, -100]))
print()

print(f(1))
print(f(2))
print(f(3))
print()

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))
print()

def f3(**keywords):
    for kw in keywords:
        print(kw, ":", keywords[kw])

f3(key1="Apple", key2="Banana", key_end="Orange")
print()

a = {"key1":"Apple", "key2":"Banana", "key_end":"Orange"}
f3(**a)
print()

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
print()

def my_function(param1: int):
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
print(my_function.__annotations__)
