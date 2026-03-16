'''
Definition : Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Approach : Sliding Window
complexity : O(n) time and O(1) space
Difficulty : Medium
youtube Link : https://www.youtube.com/watch?v=DL8LSXUsfWE&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=11
'''
class smallest_subarray :
    def min_subarray( self , target : int  , nums : list[int])-> int :
        n = len(nums)
        low , high = 0, 0
        sum = 0
        min_len = float('inf')
        while(high < n ):
            sum += nums[high]
            
            while( sum >= target):
                length = high - low + 1 
                min_len = min(min_len , length )
                sum -= nums[low]
                low += 1
            high += 1
        return min_len if min_len != float('inf') else 0
if __name__ == "__main__" :
    target = int (input("Enter the target sum : "))
    arr = [2,3,1,2,4,3]
    obj = smallest_subarray()
    print(f"The minimum length of subarray with sum greater than or equal to {target} is : {obj.min_subarray(target, arr)}")