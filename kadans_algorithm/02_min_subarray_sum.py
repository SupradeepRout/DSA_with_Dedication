class min_subarray_sum :
    def minSum(self, nums):
        n= len(nums)
        best_ans = nums[0]
        min_sum = nums[0]
        for i in range(1,n):
            v1 = best_ans + nums[i]
            v2 = nums[i]
            best_ans = min(v1,v2)
            min_sum = min(min_sum , best_ans)
        return min_sum
if __name__ == "__main__":
    arr=[2,6,8,1,4]
    obj = min_subarray_sum()
    result = obj.minSum(arr)
    print(f"The minimum subarray sum is : {result}")
    