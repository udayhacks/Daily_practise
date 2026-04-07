// Last updated: 07/04/2026, 11:41:44
class Solution {
private:
int getMaxArea(vector<int> &arr) {
        
        stack <int> st;
        int n = arr.size();
        int ans = 0 ; 
        for (int i = 0 ;i <=n;i++){
            while( !st.empty() && (i== n || arr[st.top()] >= arr[i])){
                int height  = arr[st.top()];
                st.pop();
                int length = 0;
                if( st.empty())  length = i;
                else length = i- st.top()-1;
                ans = max(ans,length*height); 
            }
            st.push(i);
        }
        return ans ;
    }

public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        
        int n = matrix.size();
        int m = matrix[0].size();
        vector<int>height(m,0);
        int maxV= 0;


        for (int i = 0 ; i <n;i++){
            for(int j = 0 ;j<m;j++){
                if (matrix[i][j] =='1') ++height[j];
                else height[j] =0;
            }
            maxV = max(maxV,getMaxArea(height));

        }
        return maxV;
    }
};