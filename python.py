class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=len(nums)
        for i in range(d-1):
            for j in range(i+1,d):
                if nums[i]+nums[j]==target:
                    return[i,j]
                
                
                    
            
                    
                        