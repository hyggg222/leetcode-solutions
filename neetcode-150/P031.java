// Search in Rotated Sorted Array
// Binary search
// Medium

// problem statement
// Given an array which was sorted in ascending order
// It has been rotated x times
// Given a target
// Return the index of target within array or -1 if it is not present

// Assume all elements are unique

public class    P031 {
    public static void main (String args[]) {
        int[] nums = {3, 4, 5, 6, 1, 2};
        int target = 1;
        Solution obj = new Solution();
        System.out.print(obj.search(nums, target));
    }
}

class Solution {
    public int search(int[] nums, int target) {
        // Optimal Solution: O(log n) 
        // Have to binary search on the given array

        // Consider the array has been rotated by any times, it is
        // always in this pattern: <ascending arr 1> <ascending arr 2> 
        // With arr 2 can be none, and elements in arr 1 are always bigger
        // than elements in arr 2

        // We can find the line between arr 1 and 2 by binary search
        // to find the first element from index 1 to n smaller than the
        // first element of the array. How to do that?
        // Let rewrite the array, put 0 if that element is bigger than nums[0]
        // and 1 if it is smaller than nums[0], that array will be in this 
        // pattern: 0 0 0 1 1 1 

        // After finding the line, we can decide which arr to binary search the target
        // If target is bigger than arr1[0] then search on arr 1
        // If target is bigger than arr2[0] and smaller than arr1[0] then search on arr 2

        int left = 1, right = nums.length - 1, line = -1;
        while (left <= right) {
            int mid = left + (right - left)/2;
            if (nums[mid] > nums[0]) {
                left = mid + 1;
            } else {
                line = mid;
                right = mid - 1;
            }
        }

        if ((line == -1 && target < nums[0]) || target < nums[line]) return -1;
        int ans = -1;
        left = (target >= nums[0] ? 0 : line);
        right = (target >= nums[0] ? line - 1 : nums.length - 1);
        while (left <= right) {
            int mid = left + (right - left)/2;
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                ans = mid;
            }
        }
        return ans;
    }
}
