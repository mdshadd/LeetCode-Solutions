nums = [5,7,7,7,8,10]
target = 7

output = [nums.index(target)]
output.append(nums[::-1].index(target))

# for i in range(0,len(nums)):
#     if nums[i]==target:
#         output.append(i)

if len(output) == 0:
    output.append(-1)
    output.append(-1)

if len(output) == 1:
    output.append(output[0])

print(output)
