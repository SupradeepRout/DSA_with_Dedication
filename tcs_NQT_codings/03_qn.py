n =int(input("Enter the size of the array : "))
s=[int(input()) for _ in range(n)]

if n==0 :
    print(0)
else:
    res= 1
    for i in range(1,len(s)):
        count = 0
        for j in range(i):
            if s[j] >= s[i] :
                break
            else:
                count += 1
        if count == i :
            res += 1
    print(f"the no of elements is :{ res}")