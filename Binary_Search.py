def binary_search(nums, k):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2#left +(right-left)//2
        if nums[mid] == k:
            return mid  
        elif nums[mid] < k:
            l = mid + 1 
        else:
            r = mid - 1  
    return -1 
n,k = map(int, input().split())
nums = list(map(int, input().split()))
result = binary_search(nums, k)
print(result)
