class A:

    ins = None

    def set(self):
        self.ins = 1

a = A()
print(a.ins)
print(A.ins)
a.set()
print(a.ins)
print(A.ins)