class subset_Sum :
    def sum(self , nums : list[int] , k)-> int :
        n = len(nums)
        pref_sum = 0 
        count = 0
        sum_count = {0:1} # to count the number of times the sum is repeated
        
        for i in range(n):
            pref_sum += nums[i]
            remove =( pref_sum - k )
            if remove in sum_count :
                count += sum_count[remove] # very important step to count the number of subarray with sum k
                
            sum_count[pref_sum] = sum_count.get(pref_sum , 0) + 1   # Update the count of current pref_sum
            
        return count
    
if __name__ == "__main__":
    print("Enter the elements of the list separated by , :- ")
    arr =list(map(int,input().split(","))) 
    k = int(input("Enter the value of k : "))
    obj = subset_Sum()
    count = obj.sum(arr , k)
    print(f"The number of subarray with sum {k} is : {count}")