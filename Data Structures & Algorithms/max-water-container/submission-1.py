class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right =len(heights)-1
        max_sum = 0
        while left<right:
            height_diff = right-left
            max_sum = max(max_sum, height_diff * min(heights[left], heights[right]))
            if heights[left] < heights[right] :
                left+=1
            else:
                right-=1
        return max_sum
        