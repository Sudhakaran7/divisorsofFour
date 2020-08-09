from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        for x in nums:
            if x == 1 or x == 2 or x == 3:
                continue
            num = 2
            temp = [1, x]
            while num ** 2 <= x:
                if len(temp) > 4:
                    break
                if not x % num:
                    if num not in temp:
                        temp.append(num)
                    if int(x/num) not in temp:
                        temp.append(int(x/num))
                num += 1
            if len(temp) == 4:
                for _ in temp:
                    sum += _
        return int(sum)
val=Solution()
nums=list(map(int,input().split()))
print(val.sumFourDivisors(nums))
