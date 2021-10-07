class Sun:
    def __init__(self):
        pass

    @classmethod
    def inst(cls):
        # x = Sun()
        if not cls:
            pass
            #cls = Sun()
        #print(cls.__sun)
        print(cls)
        return cls
        




p = Sun.inst()
f = Sun.inst()
print(p is f)


# p = Sun()
# f = Sun()
# print(p is f)