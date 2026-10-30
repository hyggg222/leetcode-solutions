public class P028 {
    public static void main (String args[]) {
        int[] nums = {-1,0,2,4,6,8};

        Solution test = new Solution();
        // 3
        System.out.println(test.search(nums, 4));
        // -1 
        System.out.println(test.search(nums, 3));
    }
}


class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left)/2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                return mid;
            }
        }

        return -1;
    }
}