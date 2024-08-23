
from threading import Thread

class Test:
    def func(self, n):
        for i in range(n):
            print("Hello World")
    @classmethod
    def func2(self, n):
        for i in range(n):
            print("This is class method")
    @staticmethod
    def func3(n): # remove self for static method
        for i in range(n):
            print("This is static method")

test = Test()
t1 = Thread(target=test.func, args=(10,))
t1.start()

t2 = Thread(target=Test.func2, args=(10,))
t2.start()

t3 = Thread(target=Test.func3, args=(10,))
t3.start()

for i in range(10):
    print("testing parallel execution")