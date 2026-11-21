class Solution {
    public boolean uniformArray(int[] nums1) {
        for (int x : nums1) {
            if (x % 2 == 1) {
                return true;
            }
        }

        for (int x : nums1) {
            if (x % 2 == 0) {
                return true;
            }
        }

        return false;
    }
}