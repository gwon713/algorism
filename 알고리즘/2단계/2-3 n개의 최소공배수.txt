class Solution {
    public int solution(int[] arr) {
        int arrLth = arr.length;
		int answer = 0;
		boolean Flag = true;
		int i=1;
		int cnt=0;
		while(true){
			answer=arr[arrLth-1]*i;
			for(int j=0; j<arrLth; j++){
				int l=1;
				Flag = true;
				while(Flag){
					if(answer == arr[j]*l){
						cnt++;
						Flag = false;
					}
					if(arr[j]*l>answer)Flag = false;
					l++;
				}
			}
			if(cnt==arrLth) break;
			cnt=0;
			i++;
		}
        return answer;
    }
}