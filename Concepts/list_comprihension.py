nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = []
# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)
# print(even_nums)

# The above for loop is written inside the list as  below
even_nums = [num for num in nums if num % 2 == 0]
print("Even nums - ", even_nums)
