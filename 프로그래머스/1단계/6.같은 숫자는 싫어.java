import java.util.ArrayList;

class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> sub = new ArrayList<Integer>();
        int var1 = -1; 

        for(int i=0; i<arr.length; i++){
            if(var1 != arr[i]){
                var1 = arr[i]; 
                sub.add(var1);
            }
        }
        answer = new int[sub.size()];
        for(int i=0; i<answer.length; i++){
            answer[i] = sub.get(i);
        }
        return answer;
    }
}