''' Definition : Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.
    Complexity : O(n) time and O(1) space
    difficulty : Easy
    approach : Sliding Window
'''
class max_subarray_sum :
    def max_sum ( self , nums : list[int] , k : int )-> int :
        sum = 0
        low , high = 0 , k-1 
        n = len(nums)
        res = float('-inf')
        
        for i in range(k):
            sum += nums[i]
        
        while(high < n):
            res = max(res, sum)
            high += 1
            low += 1 
            if(high < n ):
                sum += nums[high] - nums[low-1]
        return res 
    
if __name__ == "__main__" :
    
    k= int(input("Enter the size of subarray : "))
    #k = 2
    nums = [1, 4, 2, 10, 23, 3, 1, 15, 20]
    obj = max_subarray_sum()
    print(obj.max_sum(nums, k))