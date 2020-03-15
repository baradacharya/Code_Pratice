# Given a non decreasing  array of integers ,calculate the square of integers  while still retaining the sorted order.

# i/p      [1,2,4]

# o/p    [1,4,16]

# i/p     [-1,0,1]

# o/p    [0,1,1]

def function(nums):
    import sys
    if len(nums) == 0:
        return []

    if nums[0] >= 0:
        return [x ** 2 for x in nums]
    else:
        max_neg_ind, min_pos_ind = 0, 0

        for i in range(len(nums)):
            if nums[i] >= 0:
                min_pos_ind = i
                break
            max_neg_ind = i

        res = []

        while min_pos_ind < len(nums) and max_neg_ind >= 0:
            if nums[min_pos_ind] ** 2 <= nums[max_neg_ind] ** 2:
                res.append(nums[min_pos_ind] ** 2)
                min_pos_ind += 1
            else:
                res.append(nums[max_neg_ind] ** 2)
                max_neg_ind -= 1

        if min_pos_ind < len(nums) - 1:
            for x in range(min_pos_ind, len(nums)):
                res.append(nums[x] ** 2)

        if max_neg_ind >= 0:
            for x in range(max_neg_ind, -1, -1):
                res.append(nums[x] ** 2)

    return res


# print(function([1,2,4]))
# print(function([-1,0,1]))
print(function([-2, -1, 0, 1, 2]))



