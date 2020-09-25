import java.util.Arrays;
class Solution {
    public String solution(String s) {
	String answer = ""; 
	String[] a = s.split(" ");
	int[] i = new int[a.length];
	int j=0;
	for(String res : a){
		i[j]=Integer.parseInt(res);
		j++;
	}
	Arrays.sort(i);
	answer = i[0]+" "+i[i.length-1];
	return answer;
    }
}