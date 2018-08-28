"""
The idea is the same as Approach #3 from 295. Find Median From Data Stream.
The only additional requirement is removing the outgoing elements from the window.

Since the window elements are stored in heaps, deleting elements that are not at the top of the heaps is a pain.

At this point, an important thing to notice is the fact that if the two heaps are balanced,
only the top of the heaps are actually needed to find the medians.
This means that as long as we can somehow keep the heaps balanced, we could also keep some extraneous elements.

Thus, we can use hash-tables to keep track of invalidated elements. Once they reach the heap tops,
we remove them from the heaps. This is the lazy removal technique.

An immediate challenge at this point is balancing the heaps while keeping extraneous elements.
This is done by actually moving some elements to the heap which has extraneous elements,
from the other heap. This cancels out the effect of having extraneous elements
and maintains the invariant that the heaps are balanced.

NOTE: When we talk about keeping the heaps balanced, we are not referring to the actual heap sizes.
We are only concerned with valid elements and hence when we talk about balancing heaps, we are referring to count of such elements.
"""
"""
Two priority queues:

    A max-heap lo to store the smaller half of the numbers
    A min-heap hi to store the larger half of the numbers
A hash-map or hash-table hash_table for keeping track of invalid numbers. It holds the count of the occurrences of all such numbers that have been invalidated and yet remain in the heaps.

The max-heap lo is allowed to store, at worst, one more element more than the min-heap hi. Hence if we have processed k elements:

    If k = 2*n + 1 then lo is allowed to hold n+1 elements, while hi can hold n elements.
    If k = 2*n then both heaps are balanced and hold n elements each.
This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops of both heaps. Otherwise, the top of the max-heap lo holds the legitimate median.
"""
"""
NOTE: As mentioned before, when we are talking about keeping the heaps balanced, 
the actual sizes of the heaps are irrelevant. Only the count of valid elements in both heaps matter.
1. Keep a balance factor. It indicates three situations:

    balance = 0: Both heaps are balanced or nearly balanced.
    balance < 0: lo needs more valid elements. Elements from hi are moved to lo.
    balance > 0: hi needs more valid elements. Elements from lo are moved to hi.

2. Inserting an incoming number in_num:
    If in_num is less than or equal to the top element of lo, then it can be inserted to lo. 
        However this unbalances hi (hi has lesser valid elements now). Hence balance is incremented.

    Otherwise, in_num must be added to hi. Obviously, now lo is unbalanced. Hence balance is decremented.

Lazy removal of an outgoing number out_num:

If out_num is present in lo, then invalidating this occurrence will unbalance lo itself. 
Hence balance must be decremented.

If out_num is present in hi, then invalidating this occurrence will unbalance hi itself. Hence balance must be incremented.

We increment the count of this element in the hash_table table.

Once an invalid element reaches either of the heap tops, we remove them and decrement their counts in the hash_table table.
"""
"""
use i i+k, to mark window, element before i can be removed. 
keep <element,index> in heap.
rh will store more
"""
from heapq import *
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        lh, rh, rv = [], [], []
        # create the initial left and right heap
        #1. left heap
        for i, n in enumerate(nums[:k]):
            heappush(lh, (-n, i)) #val,index
        #right heap
        for i in range(k - k / 2):
            heappush(rh, (-lh[0][0], lh[0][1])) #val,index
            heappop(lh)
        #NOTE: As mentioned before, when we are talking about keeping the heaps balanced,
        #the actual sizes of the heaps are irrelevant. Only the count of valid elements in both heaps matter.
        #so if we are pushing and removing from same heap balance remains, otherwise imbalances
        for i, num in enumerate(nums[k:]):
            rv.append(rh[0][0] / 1. if k % 2 else (rh[0][0] - lh[0][0]) / 2.)
            if num >= rh[0][0]:#to be pushed into the right heap, gretaer than right heap min element.
                heappush(rh, (num, i + k))  # rh +1
                if nums[i] > rh[0][0]:#rh balamced
                    pass
                else:# nums[i] will be removed,it presents in lh ,lh, unbalanced;
                    heappush(lh, (-rh[0][0], rh[0][1]))
                    heappop(rh)
            else:
                heappush(lh, (-num, i + k))  # rh +1
                if nums[i] >= rh[0][0]:  # nums[i] will be removed,it presents in rh ,rh, unbalanced;
                    heappush(rh, (-lh[0][0], lh[0][1]))
                    heappop(lh)
                    # else: pass                # lh-1, balanced
            while (lh and lh[0][1] <= i): heappop(lh)  # lazy-deletion #index before i
            while (rh and rh[0][1] <= i): heappop(rh)  # lazy-deletion #index before i
        rv.append(rh[0][0] / 1. if k % 2 else (rh[0][0] - lh[0][0]) / 2.)
        return rv

s = Solution()
print s.medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)
"""
vector<double> medianSlidingWindow(vector<int>& nums, int k)
{
    vector<double> medians;
    unordered_map<int, int> hash_table;
    priority_queue<int> lo;                                 // max heap
    priority_queue<int, vector<int>, greater<int> > hi;     // min heap

    int i = 0;      // index of current incoming element being processed

    // initialize the heaps
    while (i < k)
        lo.push(nums[i++]);
    for (int j = 0; j < k / 2; j++) {
        hi.push(lo.top());
        lo.pop();
    }

    while (true) {
        // get median of current window
        medians.push_back(k & 1 ? lo.top() : ((double)lo.top() + (double)hi.top()) * 0.5);

        if (i >= nums.size())
            break;                          // break if all elements processed

        int out_num = nums[i - k],          // outgoing element
            in_num = nums[i++],             // incoming element
            balance = 0;                    // balance factor

        // number `out_num` exits window
        balance += (out_num <= lo.top() ? -1 : 1);
        hash_table[out_num]++;

        // number `in_num` enters window
        if (!lo.empty() && in_num <= lo.top()) {
            balance++;
            lo.push(in_num);
        }
        else {
            balance--;
            hi.push(in_num);
        }

        // re-balance heaps
        if (balance < 0) {                  // `lo` needs more valid elements
            lo.push(hi.top());
            hi.pop();
            balance++;
        }
        if (balance > 0) {                  // `hi` needs more valid elements
            hi.push(lo.top());
            lo.pop();
            balance--;
        }

        // remove invalid numbers that should be discarded from heap tops
        while (hash_table[lo.top()]) {
            hash_table[lo.top()]--;
            lo.pop();
        }
        while (!hi.empty() && hash_table[hi.top()]) {
            hash_table[hi.top()]--;
            hi.pop();
        }
    }

    return medians;
}
"""

        