import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n) {
        String[] s = Long.toString(n).split("");
        Arrays.sort(s,Collections.reverseOrder());
        return Long.parseLong(String.join("", s));
    }
}