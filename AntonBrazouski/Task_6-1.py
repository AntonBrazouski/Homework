class Counter:
    
    def __init__(self, *, start=0, stop=None):
        self.value = start
        self.stop = stop

    def increment(self):
        if self.stop != None:
            try:
                assert self.value < self.stop, \
                    "Max counter value is reached"
                self.value += 1
            except AssertionError as msg:
                print(msg)
            
        else:
            self.value += 1

    def get(self):
        return self.value




c = Counter(start=42)
c.increment()
print(c.get())


c = Counter()
c.increment()
print(c.get())

c.increment()
print(c.get())

c = Counter(start=42, stop=43)
c.increment()
print(c.get())

c.increment()
print(c.get())