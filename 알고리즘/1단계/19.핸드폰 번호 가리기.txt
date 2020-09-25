class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String sub = "";
		for(int i=0; i<phone_number.length()-4; i++){
			sub+="*";
		}
        answer = phone_number.replace(phone_number.substring(0,phone_number.length()-4),sub);
        return answer;
    }
}