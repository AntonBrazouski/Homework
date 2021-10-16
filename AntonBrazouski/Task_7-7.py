class MyNumberCollection():
    

    def __init__(self, *args):
        self.alist = []
        for arg in args:
            self.alist.append(arg)

    def __str__(self):
        return str(self.alist)


    def append(self, item):
        pass
        



col1 = MyNumberCollection()
print(col1)

col2 = MyNumberCollection(0, 5, 2)
print(col2)