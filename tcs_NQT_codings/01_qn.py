a ="1,3,4,5,6,6,6,7"
b = a.split(",")
lst =[int(nums) for nums in b]
#print(",".join(map (str, lst)))
print(*lst ,sep=",")

