class A:
    def __init__(self):
        self._v = "abc"

    def getV(self):
        return self._v

    def setV(self, v):
        self._v = v

    def __setattr__(self, vname, val):
        print("set", vname, val)
        if vname == "_v" or vname == "v":
            object.__setattr__(self, vname, val)
        else:
            raise Exception("{} is not allowed here".format(vname))

    def __str__(self):
        return "A._v={}".format(self._v)

    v = property(getV, setV)


a = A()
print(a.v)
a.v = 1234
print(a.v)
