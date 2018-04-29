class Solution(object):
    def findRestaurant(self, list1, list2):
        map_1 = {w:i for i,w in enumerate(list1)}
        best,res = 1e9,[]
        for i,w in enumerate(list2):
            if w in map_1:
                j = map_1[w]
                if i + j < best:
                    best = i+j
                    res = [w]
                elif i+j == best:
                    res.append(w)
        return res