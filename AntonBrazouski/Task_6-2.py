class HistoryDict:
    
    def __init__(self, adict):
        self.dict = adict
        self.stack = []
        self.stack_limit = 10
        
    def set_value(self, key, value):
        self.dict[key] = value
        self.stack.append(key)
        

    def get_history(self):
        return self.stack[-self.stack_limit:]



d = HistoryDict({"goo": 99})
d.set_value("moo1", 1)
d.set_value("moo2", 121)
d.set_value("moo3", 131)
d.set_value("moo4", 113)
d.set_value("moo5", 141)
d.set_value("moo6", 151)
d.set_value("moo7", 161)
d.set_value("moo8", 711)
d.set_value("moo9", 181)
d.set_value("moo10", 181)
d.set_value("moo11", 11)
d.set_value("moo12", 1121)
print(d.get_history())
