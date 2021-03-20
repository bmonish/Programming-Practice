class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        if (x < 10) return true;
        
        int temp = x;
        int reverse = 0;
        
        while (temp > 0) {
            reverse = 10 * reverse + temp % 10;
            temp /= 10;
        }
        
        if (reverse == x) return true;
        else return false;
    }
}