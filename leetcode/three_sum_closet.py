
from typing import List

class Solution:
    # while loop three index
    def threeSumClosest_1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0

        i, j, k = 0, 1, 2
        if n == 3:
            return nums[i] + nums[j] + nums[k]

        diff = float('inf')
        res = 0

        while i < n - 2:
            print(i, j, k, end='\n')
            t = nums[i] + nums[j] + nums[k]
            print(f"Sum: {t}", end=', ')
            # exact same value
            if t == target: return t

            if abs(t - target) < diff:
                diff = abs(t - target)
                res = t
                print(diff, res)

            k +=1

            if j < n-2 and k > n-1:
                j +=1
                k = j+1
            elif j >= n-2:
                i+=1
                j = i+1
                k = j+1


        return res

# binary search
    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
            if not nums:
                return None

            diff = float('inf')
            res = float('inf')
            nums.sort()

            for i in range(len(nums) - 2):
                p1 = i + 1
                p2 = len(nums) - 1

                while p1 < p2:
                    s = nums[i] + nums[p1] + nums[p2]
                    if abs(s - target) < diff:
                        diff = abs(s - target)
                        res = s
                    
                    if s < target:
                        p1 +=1
                    elif s > target:
                        p2 -=1
                    else:
                        return target
            return res