class Solution:
    def maxFrequency(self,nums, k):
        nums.sort()  # Step 1: Sort the array
        left = 0
        total = 0
        max_freq = 0

        # Step 2: Use sliding window
        for right in range(len(nums)):
            # Add the value at nums[right] to total window cost
            total += nums[right]

            # Check if current window is valid
            # (window size * current max number) should not exceed total + k
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]  # Remove the leftmost value
                left += 1            # Shrink the window

            # Update max frequency
            max_freq = max(max_freq, right - left + 1)

        return max_freq

        