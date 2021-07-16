import java.util.Collections;
import java.util.Arrays;

class Solution{
    public int solution(int []A, int []B)
    {
        int answer = 0;
		Integer b2[] = Arrays.stream(B).boxed().toArray(Integer[]::new);
		Arrays.sort(A);
		Arrays.sort(b2,Collections.reverseOrder());
		
		for(int i=0; i<A.length; i++){
			answer += A[i]*b2[i];
		}
        return answer;
    }
}