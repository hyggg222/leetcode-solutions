// Koko Eating Bananas
// Binary Search - Medium

// Optimal Solution - O(n * log(n))
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = 0;
        for (int pile : piles) max = Math.max(max, pile);
        int left = 1, right = max, ans = max;
        while (left <= right) {
            int mid = left + (right - left)/2;
            long time = 0;
            for (int pile : piles) {
                if (pile % mid == 0) time += pile/mid;
                else time += pile/mid + 1;
            }
            if (time <= h) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            } 
        }
        return ans;
    }
}
