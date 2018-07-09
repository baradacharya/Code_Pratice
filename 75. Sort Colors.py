#put 0, 1, 2 in seq
#i, end of 0, end of 1
#default replace by 2 then replace by 1, then replace by 0
def sortColors(nums):
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
        print nums,i,j

sortColors([2,0,2,1,1,0])
"""
[2, 0, 2, 1, 1, 0] 0 0
[0, 2, 2, 1, 1, 0] 1 1
[0, 2, 2, 1, 1, 0] 1 1
[0, 1, 2, 2, 1, 0] 1 2
[0, 1, 1, 2, 2, 0] 1 3
[0, 0, 1, 1, 2, 2] 2 4
"""