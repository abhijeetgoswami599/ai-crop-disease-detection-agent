from collections import Counter

def findLHS(nums: list[int]) -> int:
    """
    Finds the length of the longest harmonious subsequence in an integer array.
    """
    # Step 1: Count the occurrences of each number.
    count = Counter(nums)
    ans = 0

    # Step 2: Iterate through the unique numbers in the counter.
    for num, freq in count.items():
        # Step 3: Check if num + 1 also exists in the counter.
        if (num + 1) in count:
            # If it exists, a harmonious subsequence can be formed by all occurrences
            # of 'num' and 'num + 1'. Update the maximum length found so far.
            ans = max(ans, freq + count[num + 1])

    # Step 4: Return the maximum length.
    return ans

# Example Usage:
nums1 = [1, 3, 2, 2, 5, 2, 3, 7]
print(f"Input: {nums1}")
# The longest harmonious subsequence is [3, 2, 2, 2, 3] (or [2, 2, 2, 3, 3])
print(f"Output: {findLHS(nums1)} \n") # Output: 5

nums2 = [1, 2, 3, 4]
print(f"Input: {nums2}")
print(f"Output: {findLHS(nums2)} \n") # Output: 2

nums3 = [1, 1, 1, 1]
print(f"Input: {nums3}")
print(f"Output: {findLHS(nums3)} \n") # Output: 0
