class Employee:
    def __init__(self,ne):
        self.ne = ne
    def calc(self):
        zarpl = 0
        return zarpl
class Manager(Employee):
    def __init__(self,ne,k,h):
        super().__init__(ne)
        self.k = k
        self.h = h
    def calc(self):
        zarpl = self.k + self.h
        return zarpl
class Developer(Employee):
    def __init__(self,ne,j,f):
        super().__init__(ne)
        self.j = j
        self.f = f
    def calc(self):
        zarpl = self.j * self.f
        return zarpl
