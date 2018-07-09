#https://leetcode.com/problems/task-scheduler/solution/
#priorty queue
#We need to arrange the task s.t. each same task is n distance apart
#Idea is to add them to a priority Q and sort based on the highest frequency.
#And pick the task in each round of 'n' with highest frequency.
# As you pick the task, decrease the frequency, and put them back after the round.
#similar 358 https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
#T: O(nlogn)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        time  = 0
        import heapq
        import collections
        counter = collections.Counter(tasks)
        heap = [-c for c in counter.values()] #Maxheap so negative value
        heapq.heapify(heap)
        while heap :
            freq_temp = []#will store updated frequency
            #heapification occurs only after the intervals of cooling time, n, as done in the last approach.
            for _ in range(n+1):#min gap n so n+1 time
                time += 1
                if heap:
                    freq = heapq.heappop(heap)
                    if freq < -1: #freq > 1, freq -ve
                        freq_temp.append(freq+1) #freq-1 since freq -ve + 1
                if not heap and not freq_temp:
                    break
            for f in freq_temp:
                heapq.heappush(heap,f)

        return time

s = Solution()
print s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)



