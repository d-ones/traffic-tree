class Tree(object):
    def __init__(self, value, children=None):
        self.value = value
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def haspath(self, arr, x):
        arr.append(self.value)  
        check = [key for key, value in self.value.items()][0]
        if (check == [key for key, value in x.value.items()][0]):    
            return True
        for child in self.children:
            if child.haspath(arr, x):
                return True
        arr.pop(-1)
        return False
    def printpath(self, x):
        arr = []
        arr2 = []
        if (self.haspath(arr, x)):
            for i in arr:
                arr2 += (key for key, value in i.items())
            for i in range(len(arr2) - 1, 0, -1):
                print(arr2[i], end = "->")
            print(arr2[0])
        else:
            print("No Path")
    def turn_ratio(self, x):
        arr = []
        if (self.haspath(arr, x)):
            math = []
            for intersection in arr:
                for key, value in intersection.items():
                    math.append(intersection[key])
            ratio = (math[len(math)-1]/math[1])
            if ratio <= 1:
                print(ratio)
            elif ratio > 1:
                print(f'Ratio is above 1 ({ratio}): Correct Node?')
        else:
            print('No Ratio')

left = Tree({'intersection2': 1})
middle = Tree({'intersection3': 2})
right = Tree({'intersection4': 8})
root = Tree({'intersection1': 4})
root.children = [left, middle, right]


leftturn_columbia = Tree({'intersection6': 2})
right2 = Tree({'intersection5': 3}, [leftturn_columbia, Tree({'intersection7': 9})])
right.children = [right2]


# root (1)
# /|\
#2 3 4 (8)
#     \
#      5 (3)
#      /\
#     6  7

root.printpath(right2)
root.turn_ratio(leftturn_columbia)
