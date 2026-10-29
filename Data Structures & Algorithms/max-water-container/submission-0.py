class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        ans=float("-inf")
        r=len(heights)-1
        while l<r:
            area=(r-l)*min(heights[l],heights[r])
            ans=max(ans,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return ans
        