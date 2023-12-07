def majorityElement(nums):
    if not nums:
        return []
    candidate1, candidate2, count1, count2 = 0, 1, 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    result = []
    n = len(nums)
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)
    return result
nums = list(map(int, input("Enter the integers separated by spaces: ").split()))
result = majorityElement(nums)
print("Output:", result)
