class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> words = new HashSet(wordDict);
        boolean [] dp = new boolean[s.length()+1];

        dp[0] = true;

        for(int j = 1;j<=s.length();j++){
            for(int i=0;i<j;i++){
                if(dp[i] && words.contains(s.substring(i,j))){
                    dp[j] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
        
    }
}