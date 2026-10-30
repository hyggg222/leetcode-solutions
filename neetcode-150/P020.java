// Neetcode 150
// Type: Binary Search 
// Num 28 - Search a 2D Matrix
// Medium

public class P028{
    public static void main (String args[]) {
        // Run test case
        int[][] matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};

        Solution solution = new Solution();
        boolean result = solution.searchMatrix(matrix, 3);
        System.out.println(result);
        boolean result1 = solution.searchMatrix(matrix, 13);
        System.out.println(result1);
    }
}

class FirstSolution {
    public boolean searchMatrix(int[][] matrix, int target) {   
        int n = matrix.length;
        int m = matrix[0].length;

        int[] arr = new int[n * m];
        for (int i = 0, cnt = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                arr[cnt++] = matrix[i][j];
            }
        }
        
        int left = 0, right = n * m - 1;
        while (left <= right) {
            int mid = left + (right - left)/2;
            if (arr[mid] < target) {
                left = mid + 1;
            } else if (arr[mid] > target) {
                right = mid - 1;
            } else {
                return true;
            }
        } 
        return false;
    }
}

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix.length;
        int m = matrix[0].length;

        int left = 0, right = m * n - 1;
        while (left <= right) {
            int mid = left + (right - left)/2;

            int row = mid / m;
            int col = mid % m;
            if (matrix[row][col] < target) {
                left = mid + 1;
            } else if (matrix[row][col] > target) {
                right = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }   
}

