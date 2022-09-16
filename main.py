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
                    math.append(value)
            ratio = (math[len(math)-1]/math[1])
            print(ratio)
        else:
            print('No Ratio')
    def balancing(self):
        total_children = 0
        total_self = 0
        for key, value in self.value.items():
            total_self += value
        for child in self.children:
            for key, value, in child.value.items():
                total_children += value
        if total_children == total_self:
            print('Balanced')
        else:
            print(f'Unbalanced :/ (value is {total_self}, total is {total_children})')


#     exit
#   /      \ 
# ebr      wbfi9 -------- exit feeders
#         /  |    \
#      wblc wbfi10 wbrc - wbfi9 feeders

wblc = Tree({'westbound left columbia': 63})

wbfi9_feeders = [wblc, 
            Tree({'westbound franklin intersection 10': 504}),
             Tree({'westbound right columbia': 112})]
wbfi9 = Tree({'westsbound franklin intersection 9': 674}, wbfi9_feeders)
exit_feeders = [Tree({'eastbound right intersection 9': 4}), wbfi9]
exit_east_driveway = Tree({'exit_east_driveway': 543}, exit_feeders)
