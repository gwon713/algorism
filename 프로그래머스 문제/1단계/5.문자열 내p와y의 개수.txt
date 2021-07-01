class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;

        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == 'p' || s.charAt(i) == 'P') {
                p++;
            }
            if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') {
                y++;
            }
        }

        if (p != y) {
            answer = false;
        }

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");

        return answer;
    }
}