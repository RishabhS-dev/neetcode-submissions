class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0, len(numbers)-1
        while l<r:
            curssum = numbers[l]+numbers[r]
            if curssum > target:
                r-=1
            elif curssum < target:
                l+=1
            else:
                return[l+1,r+1]
        return[]
        