nums = [1, 2, 3]

nums.append(3)
nums.append(3)
nums[3] = 100 #Altera um elemento 
nums.insert(0, -200) #insere e desloca 
print(nums)

print(nums[5])
print(nums[-1])

print(len(nums))