nums = [1,2,1, 4]
compare =[]
for  num in nums:
    if num in compare:
        print(num)
        break
    else:
        compare.append(num)