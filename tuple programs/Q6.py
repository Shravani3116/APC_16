nums = (1,2,3,4,5,1,2,3,7,8,4,5,8,10,1,2,3,8,9,10)
num=int(input("Enter a number to check its frequency in the tuple: "))
count=0
for i in nums:
    if i==num:
        count+=1
print("Frequency of",num,"in the tuple is:",count)