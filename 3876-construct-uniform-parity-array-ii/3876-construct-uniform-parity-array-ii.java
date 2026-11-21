class Solution {
    public boolean uniformArray(int[] nums1) {
        int min = nums1[0];

        for (int x : nums1) {
            min = Math.min(min, x);
        }

        if ((min & 1) == 1) {
            return true;
        }

        for (int x : nums1) {
            if ((x & 1) == 1) {
                return false;
            }
        }

        return true;
    }
}