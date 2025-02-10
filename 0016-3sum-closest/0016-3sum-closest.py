class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Two-pointer approach
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                # Update the closest sum if needed
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    left += 1  # Move left pointer to increase sum
                elif curr_sum > target:
                    right -= 1  # Move right pointer to decrease sum
                else:
                    return curr_sum  # Exact match found, return immediately

        return closest_sum