import java.util.ArrayList;
import java.util.Collections;

class Solution {
  public int[] solution(int[] arr, int divisor) {
      ArrayList<Integer> integer = new ArrayList<Integer>();

          for(int i = 0 ; i <arr.length ; i++) {
              if(arr[i] % divisor == 0) {
                  integer.add(arr[i]);
              }
          }

          if(integer.size() == 0) {
              integer.add(-1);
          }
          int[] answer = new int[integer.size()];
          Collections.sort(integer);
          for(int i = 0 ; i < integer.size();i++) {
              answer[i]=integer.get(i);
          }

          return answer;
  }
}