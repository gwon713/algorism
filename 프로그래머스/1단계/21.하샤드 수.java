class Solution {
    public boolean solution(int x) {
        int hsd = x;
        int xtotal = 0;
        while(true){
            xtotal += hsd%10;
            if(hsd/10==0) break;
            hsd/=10;
        }
        return x%xtotal==0 ? true:false;
    }
}