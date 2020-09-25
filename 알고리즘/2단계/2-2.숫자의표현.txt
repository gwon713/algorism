class Solution {
    public int solution(int n) {
        int answer = 0;
        int total = 0;
        for(int i=1; i<=n; i++){
            for(int j=i; j<=n; j++){
                total += j;
                if(total == n){
                    answer++;
                    total = 0;
                    break;
                }else if(total > n){
                    total=0;
                    break;
                }
            }
        }
        return answer;
    }
}