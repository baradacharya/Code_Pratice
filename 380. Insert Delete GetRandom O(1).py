##keep a list and hash map<value, index>
##while dleteing swap the value with the last element and then delete
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.index_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            return False
        else:
            self.vals.append(val)
            self.index_map[val] = len(self.vals)-1
            return

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            ind = self.index_map[val]
            self.vals[ind],self.vals[-1] = self.vals[-1],self.vals[ind]
            self.index_map[self.vals[ind]] = ind
            del self.index_map[val]
            self.vals.pop()
            return
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return self.vals[random.randint(0,len(self.vals)-1)]




# Your RandomizedSet object will be instantiated and called as such:
randomSet =  RandomizedSet();
print randomSet.insert(1)
print randomSet.remove(2)
print randomSet.insert(2)
print randomSet.getRandom()
print randomSet.remove(1)
print randomSet.insert(2)
print randomSet.insert(1)
print randomSet.insert(3)
print randomSet.getRandom()