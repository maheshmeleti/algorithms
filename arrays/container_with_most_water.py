'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by 
array [1,8,6,2,5,4,8,3,7]. In this case, the 
max area of water (blue section) the container can contain is 49.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # find max product of [j-i] and min(arr[j], arr[i])
        i = 0; j = len(height) - 1;
        res = (j - i) * min(height[j],height[i])
        
        while i < j:
            res = max(res, (j - i) * min(height[j],height[i]))
            if height[j] < height[i]: #explore bigger height from right
                j -= 1
            else:
                i += 1
        
        return res
