import random
import binarytree
from binarytree import Node as bNode

SP = 20

class Node(bNode):
    def __init__(self, value, data=None, left=None, right=None):
        bNode.__init__(self, value, left, right)
        if data:
            self.data = data
        else:
            self.data = str(value)

def buildRandomMap():
    m = []
    while True:
        m.append([random.randint(0, SP), random.randint(0, SP)])
        t = map2tree(m)
        if len(t) == len(m):
            m.pop()
        elif len(m) == SP:
            return m

def map2tree(m):
    root = Node(m[0][0])
    while True:
        noChange = True
        fathers = root.preorder
        for t in m:
            for f in fathers:
                #print("2f")
                if t[0] == f.value:
                    noChange &= not addNode(root, f, Node(t[1]))
        if noChange:
            return root

# left is child for postorder, return true if added
def addNode(root, father, child):
    for r in root.preorder:
        if child.value == r.value:
            return False
    if not father.left:
        father.left = child
        return True
    else:
        otherchild = father.left
        while True:
            if child.value == otherchild.value:
                return False
            elif otherchild.right:
                otherchild = otherchild.right
            else:
                break
        otherchild.right = child
        return True

def sumTree(p):
    t = binarytree.build(p.values)
    for node in t.postorder:
        if node.left:
            node.value += node.left.value
        if node.right:
            node.value += node.right.value
    return t
            
fixmap = [[2, 75], [75, 85], [85, 50], [50, 15], [2, 132], [50, 96], [50, 134], [2, 44], [50, 11], [75, 47], [85, 22], [44, 140], [85, 81], [11, 113], [50, 102], [22, 51], [81, 74], [140, 83], [134, 61], [83, 38], [140, 62], [81, 58], [96, 52], [50, 86], [132, 19], [38, 110], [83, 13], [61, 69], [86, 108], [74, 131], [19, 119], [86, 37], [50, 124], [81, 92], [85, 26], [58, 116], [140, 114], [22, 42], [75, 118], [110, 8], [42, 30], [47, 23], [19, 106], [134, 73], [134, 54], [134, 133], [22, 125], [118, 70], [38, 71], [92, 115], [96, 136], [26, 9], [11, 129], [129, 126], [126, 82], [73, 90], [108, 117], [70, 40], [19, 31], [23, 25], [115, 100], [86, 60], [140, 121], [85, 80], [13, 93], [108, 57], [133, 78], [19, 1], [81, 17], [19, 48], [25, 101], [125, 21], [136, 10], [54, 94], [129, 32], [15, 135], [121, 46], [108, 7], [30, 91], [115, 18], [40, 76], [100, 0], [47, 77], [81, 95], [52, 104], [92, 72], [106, 45], [115, 63], [110, 49], [124, 3], [108, 138], [26, 43], [21, 127], [54, 24], [124, 59], [93, 20], [3, 14], [125, 97], [54, 27], [61, 53], [9, 5], [114, 29], [69, 39], [1, 89], [116, 68], [91, 123], [74, 112], [11, 107], [115, 33], [80, 35], [83, 99], [32, 41], [89, 139], [132, 84], [9, 55], [63, 137], [48, 122], [51, 6], [17, 4], [137, 103], [60, 65], [46, 28], [3, 88], [45, 98], [33, 79], [131, 105], [127, 87], [46, 109], [72, 16], [114, 64], [15, 67], [136, 12], [125, 56], [88, 130], [131, 120], [73, 66], [33, 34], [93, 128], [1, 36], [19, 111]]
#print(map2tree(fixmap))
#print(sumTree(map2tree(fixmap)))

mymap = buildRandomMap()
print(mymap)
mytree = map2tree(mymap)
mysumtree = sumTree(mytree)
print(mytree)
print(mysumtree)
