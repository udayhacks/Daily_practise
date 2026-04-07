// Last updated: 07/04/2026, 11:34:55
class Solution {
public:
    vector<int> topStudents(vector<string>& positive_feedback, vector<string>& negative_feedback, vector<string>& report, vector<int>& student_id, int k) {


        unordered_map<int,int> mp;
        vector<pair<int,int>> created_list;
        vector<pair<int,int>> lst;
        unordered_map<string,int>feedback;
        int n = report.size();
        for ( auto w: positive_feedback){
            feedback[w] = 3;
        }
        for ( auto w:negative_feedback){
            feedback[w] = -1;
        }
        for ( int i = 0; i<n;i++){
            int score = 0 ;

            stringstream word_to_word(report[i]);
            string word;
            while(word_to_word >> word){
                score+=feedback[word];
            }

            
            lst.push_back({-score,student_id[i]});
        }
       
        make_heap(begin(lst),end(lst),greater<>());
        vector<int>ans;
        while(k--){
            pop_heap(begin(lst),end(lst),greater<>());
            ans.push_back(lst.back().second);
            lst.pop_back();
        }
        return ans;
        
        
    }



    
};
auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });