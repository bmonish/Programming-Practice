import java.util.Arrays;

class Solution {
    public int[] sortedSquares(int[] nums) {
        int i;
        int[] sortedArray = new int[nums.length];
        for (i = 0; i < nums.length; i++){
            sortedArray[i] = nums[i] * nums[i];
        }
        
        Arrays.sort(sortedArray);
        return sortedArray;
    }
}