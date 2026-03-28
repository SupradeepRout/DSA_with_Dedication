'''
compare * and # present in a string and return true if the count is same'''
from collections import Counter
s =input("Enter the string ")
count = Counter(s)
diff = count.get("*",0) - count.get("#",0)
if diff == 0 :
    print("the string is valid")
else :
    print(f"the differce btwn * & # is :{diff}")


