class EvenRange:

    def __init__(self, start, end):
        self.n = start
        self.end = end
        
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.end:
            print(f"self.n = {self.n}")
            if self.n % 2 != 0:
                self.n += 1
            result = self.n
            self.n += 2
            #print(self.n)
            return result
        else:
            raise StopIteration            
            # try:
            #     raise StopIteration
            #     assert StopIteration, "out of numbers"

            # except StopIteration as msg:
            #     print(msg)



er1 = EvenRange(7,11)
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))

er2 = EvenRange(3, 14)
for number in er2:
    print(number)