class Solution {
public:
    int feasible(vector<int> piles,int k,int h){
        long long time=0;
        for(int i=0;i<piles.size();i++){
               time+=(piles[i]-1)/k+1;
        }
        return time<=h;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        long long l=1,r=*max_element(piles.begin(),piles.end());
        while(l<=r){
            int mid=l+(r-l)/2;
            if(feasible(piles,mid,h)){
                r=mid-1;
            }else {
               l=mid+1;
                
            }
        }
        return l;
    }
};