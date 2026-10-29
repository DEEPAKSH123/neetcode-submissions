class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit=set()
        for n in nums:
            if n not in visit:
                visit.add(n)
            else:
                return True
        return False