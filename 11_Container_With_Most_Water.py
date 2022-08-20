# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

#LEVEL - MEDIUM

class Solution:
    def maxArea(self, height):
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res
