"""
Triplet Sum Smaller

Definition:
Given an array of integers and a target sum, count the number of triplets (i, j, k) where i < j < k
and arr[i] + arr[j] + arr[k] < target sum.

Algorithm:
1. Sort the array in ascending order.
2. For each element at index i (from 0 to n-3):
   - Initialize left pointer at i+1 and right pointer at n-1.
   - While left < right:
     - Calculate the sum of arr[i] + arr[left] + arr[right].
     - If sum >= target, decrement right (to reduce sum).
     - Else, all elements from left to right-1 will form valid triplets with i,
       so add (right - left) to count and increment left.
3. Return the total count.

Time Complexity: O(n^2) - O(n log n) for sorting + O(n^2) for the two-pointer traversal.

Difficulty Level: Medium

Platform: GFG
Link :https://www.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1
"""

class triplet_with_smaller_sum:
    def count_triplet(self ,n , sum  , arr: list[int]) -> int :
        arr.sort()
        count=0
        
        for  i in range (n-2):
            left = i+1 
            right= n-1
            
            while(left < right):
                total= arr[i] + arr[left] + arr[right]
                if(total >= sum):
                    right -=1
                else:
                    count += (right - left)
                    left += 1   
        return count
    
if __name__=="__main__":
    arr=[5,1,3,4,7]
    print(triplet_with_smaller_sum().count_triplet(len(arr), 12, arr))
    
    

                    
        