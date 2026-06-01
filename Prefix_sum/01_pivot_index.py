'''
Definition : Given an array of integers, return the "pivot" index of this array.The pivot index is the index where the sum of 
the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
Approach : Prefix Sum
Time Complexity : O(n) where n is the length of the array
Space Complexity : O(1)
Difficulty : Easy
problem Link : https://leetcode.com/problems/find-pivot-index/description/
YouTube Link : https://youtu.be/F86WfZ5RUC8?si=KUy6y8zD_OOS5uMD
'''



class find_pivot_element:
    def find_pivot(self , nums: list[int])-> int:
        pref_sum = 0
        sum_list = sum(nums)
        n = len(nums)
        
        for i in range(n):
            suff_sum = sum_list - pref_sum - nums[i]  # SUM_List = pref_sum[i] + suff_sum[i] + arr[i] 
            
            if pref_sum == suff_sum :
                return i
            
            pref_sum += nums[i] # update after check the condition . So the calculation is consider for next index 
            
        return -1 
if __name__=="__main__":
    print("Enter the elements of the list separated by , :- ")
    arr =list(map(int,input().split(","))) 
    obj = find_pivot_element()
    pivot_index = obj.find_pivot(arr)
    print(f"The pivot index is : {pivot_index}")
    