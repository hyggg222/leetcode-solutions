// Find Minimum in Rotated Sorted Array
// Binary Search
// Medium

class Solution {
    public int findMin(int[] nums) {
        // The array has alr been rotated
        // The array is sorted in ascending order in the beginning
        // All elements in array are unique
        // Return the minimum element
        // Optimal Time Complexity: O(log n)

        // Simple Solution - O(n * log n)
        // Sort the array then binary search the element

        /*
        Arrays.sort(nums);
        return nums[0];
        */

        // Suggested Solution - O(n)
        // Should not sort the array 

        // Insight: If we rotate the array at any times
        // The array is alway in this pattern: 
        // [Ascending Array 1] [Ascending Array 2] 
        // Array 2 can be none
        // Array 1 is always larger than array 2
        // How we can find the position between 2 arrays
        // -> Find the first element that is smaller than the first element 
        // -> Simple loop 
        
        /*
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[0]) {
                return nums[i];
            }
        }
        // if the array 2 is none, return the first element of array 1
        return nums[0];
        */

        // Optimal Solution - O(log n)
        // Binary search on the rotated array

        // Rewrite the array start from index 1
        // Let 0 is bigger than nums[0], 1 is smaller than nums[0]
        // Array pattern: 1 1 1 1 0 0 0
        // Can binary search on this

        
        int left = 1, right = nums.length - 1, ans = nums[0];
        while (left <= right) {
            int mid = left + (right - left)/2;
            if (nums[mid] > nums[0]) {
                left = mid + 1;
            } else {
                ans = nums[mid];
                right = mid - 1;
            }
        }
        return ans;
    
    }
}
