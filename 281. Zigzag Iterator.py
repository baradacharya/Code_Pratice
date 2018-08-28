import itertools
#With a generator function and a down counter:
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        def vals():
            # for i in itertools.count():#counter
            for i in range(max(len(v1),len(v2))):
                for v in v1, v2:
                    if i < len(v):#if counter less than length of list
                        yield v[i]
        self.vals = vals()
        self.n = len(v1) + len(v2)

    def next(self):
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        return self.n > 0

i, v = ZigzagIterator([1,2],[3,4,5,6]),[]
while i.hasNext(): v.append(i.next())
print v

