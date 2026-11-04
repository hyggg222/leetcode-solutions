// Search in Rotated Sorted Array
// Binary search
// Medium

// problem statement
// Given an array which was sorted in ascending order
// It has been rotated x times
// Given a target
// Return the index of target within array or -1 if it is not present

// Assume all elements are unique

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
        // If target is bigger than arr2[0] and smaller than arr1[0] then search on arr
        // 2

        /*
         * 
         * int left = 1, right = nums.length - 1, line = -1;
         * while (left <= right) {
         * int mid = left + (right - left)/2;
         * if (nums[mid] > nums[0]) {
         * left = mid + 1;
         * } else {
         * line = mid;
         * right = mid - 1;
         * }
         * }
         * 
         * int ans = -1;
         * if (line == -1 || target >= nums[0]) {
         * if (target < nums[0]) return -1;
         * left = 0;
         * right = (line != -1 ? line - 1 : nums.length - 1);
         * while (left <= right) {
         * int mid = left + (right - left)/2;
         * if (nums[mid] > target) {
         * right = mid - 1;
         * } else if (nums[mid] < target) {
         * left = mid + 1;
         * } else {
         * ans = mid;
         * break;
         * }
         * }
         * } else {
         * if (line == -1) return -1;
         * left = line;
         * right = nums.length - 1;
         * while (left <= right) {
         * int mid = left + (right - left)/2;
         * if (nums[mid] > target) {
         * right = mid - 1;
         * } else if (nums[mid] < target) {
         * left = mid + 1;
         * } else {
         * ans = mid;
         * break;
         * }
         * }
         * }
         * return ans;
         */

        // More optimal solution
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
                return mid;

            // Check which segment is ascending, at least one is ascending because there is
            // only one line
            // If one segment is ascending, we know is target in that segment or not
            if (nums[left] <= nums[mid]) {
                if (target < nums[mid] && target >= nums[left]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
}
