"""
- if the starting element is 0, then left pointer will be at 0 and right will move to find the first non-zero element
- if the starting element is non-zero then it will be swapped with itself and right and left will be incremented, until left points to the first non-zero element
"""

def moveZeroes(nums) -> None:
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    
    return nums

print(moveZeroes([1, 0, 3]))
