class MySquareIterator:
    
    def __init__(self, alist):
        self.storage_list = alist

    def __iter__(self):
        return iter(self.storage_list)

    def __next__(self):
        pass


lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
