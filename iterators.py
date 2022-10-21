
class Iterators:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num <=5:
            x=self.num
            self.num= self.num+1
            return x
        else:
            raise StopIteration

myClass = Iterators()
myIterator = iter(myClass)
a=20
for x in range(a):
    print(next(myIterator))