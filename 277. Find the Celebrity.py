"""
The first loop is to exclude n - 1 labels that are not possible to be a celebrity.
After the first loop, x is the only candidate.
The second and third loop is to verify x is actually a celebrity by definition.

The key part is the first loop. To understand this you can think the knows(a,b)
as a a < b comparison, if a knows b then a < b, if a does not know b, a > b.
Then if there is a celebrity, he/she must be the "maximum" of the n people.

However, the "maximum" may not be the celebrity in the case of no celebrity at all.
Thus we need the second and third loop to check if x is actually celebrity by definition.

"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        #trick if a < b and a knows b, a can't be candidate.
        #so switch candidate until you find some one who doesn't know afterwards.
        #in some case b < c, if b knows c then c can't be candidate any way.
        for i in range(n):
            if knows(candidate,i):
                candidate = i
        for i in range(candidate):#already searched from [candidate,n],now search from [0,candidate]
            if knows(candidate,i):
                return -1
        for i in range(n):#check candidate shouldn't know anyone
            if not knows(i,candidate):
                return -1
        return candidate