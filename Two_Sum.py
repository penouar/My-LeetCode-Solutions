class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict=dict()
        for i in range(len(nums)):
            difference=target-nums[i]
            if difference in myDict:
                return [myDict.get(difference), i]
            else:
                myDict[nums[i]]=i
