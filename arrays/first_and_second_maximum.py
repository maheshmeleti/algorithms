
class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, sizeOfArray, arr):
        
        
        # Your code here'''
        # Function should return a list containing two elements'''
        # li = [maximum, second_maximum]
        max = arr[0]
        second_max = -1
        for i in range(1, sizeOfArray):
            #rint(i, max, second_max)
            if arr[i] > max:
                second_max = max
                max = arr[i]
                
                
            elif arr[i] != max:
                if arr[i] > second_max:
                    second_max = arr[i]
        
        return max, second_max
