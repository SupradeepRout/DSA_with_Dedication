class sbarray_sum_divid_by_k:
    def sum(self ,  nums :list[int] , k ):
        n = len(nums)
        sum = 0
        count = 0
        rem_count = {} # to count the frequency of remainders
        rem_count[0] = 1 # to count the subarray which is divisible by k from the start
        
        for i in range(n):
            sum += nums[i]
            reminder = sum % k
            if reminder in rem_count :
                count += rem_count[reminder] # very important step to count the number of subarray with sum divisible by k
            rem_count[reminder] = rem_count.get(reminder ,0 ) + 1 # Update the count of current reminder
        return count
    # Here , In the hash map we are storing the reminder of the sum with k and its frequency.not the sum itself because we are 
    # interested in the subarray which is divisible by k and if the reminder is same for two different sums then it means that 
    # the subarray between those two sums is divisible by k.
if __name__ == "__main__":
    k = int(input("enter the value of k :"))
    print("Enter the array elements :")
    arr =list(map(int,input().split(",")))
    print(arr)
    obj = sbarray_sum_divid_by_k()
    result = obj.sum(arr,k)
    print(f"Count of subarray which is divisible by {k} is {result}")