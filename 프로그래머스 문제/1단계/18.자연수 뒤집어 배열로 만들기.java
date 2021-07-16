class Solution {
    public int[] solution(long n) {
        String snum = String.valueOf(n);
        int[] answer = new int[snum.length()];
        for(int i=0; i<snum.length(); i++){
            answer[i] = (int) (n%10);
            n/=10;
        }
        return answer;
    }
}