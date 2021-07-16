import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++) {
            int length = commands[i][1] - commands[i][0] + 1;
            int[] arr = new int[length];


            for(int j=0; j<length; j++) {
                arr[j] = array[commands[i][0] - 1 + j];
            }

            Arrays.sort(arr);
            answer[i] = arr[commands[i][2] - 1];
        }

        return answer;
    }
}