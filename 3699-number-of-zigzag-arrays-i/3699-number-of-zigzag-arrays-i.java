class Solution {
    static final int MOD = 1_000_000_007;

    public int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;

        long[] up = new long[m];
        long[] down = new long[m];

        for (int i = 0; i < m; i++) {
            up[i] = 1;
            down[i] = 1;
        }

        for (int len = 2; len <= n; len++) {
            long[] nextUp = new long[m];
            long[] nextDown = new long[m];

            long sum = 0;
            for (int i = m - 1; i >= 0; i--) {
                nextUp[i] = sum;
                sum += down[i];
                if (sum >= MOD) sum -= MOD;
            }

            sum = 0;
            for (int i = 0; i < m; i++) {
                nextDown[i] = sum;
                sum += up[i];
                if (sum >= MOD) sum -= MOD;
            }

            up = nextUp;
            down = nextDown;
        }

        long ans = 0;
        for (int i = 0; i < m; i++) {
            ans += up[i];
            ans += down[i];
            ans %= MOD;
        }

        return (int) ans;
    }
}