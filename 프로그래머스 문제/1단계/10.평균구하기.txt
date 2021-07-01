class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int rs=0;
        for(int i=0; i<arr.length; i++){
            rs+=arr[i];
        }
        answer = (double)rs/arr.length;
        return answer;
    }
}