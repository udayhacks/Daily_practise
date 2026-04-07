// Last updated: 07/04/2026, 11:41:13

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector < vector <string> > res;
        vector <string> path;
        func(s, 0, path, res);
        return res;
    }


    void func(string s, int index, vector<string>& path, vector<vector<string> >& res) {
        if (index == s.size()) {
            res.push_back(path);
            return;
        }
    


        for (int i = index; i < s.size();i++) {
            
            if (is_pal(s, index, i)) {
                path.push_back(s.substr(index, i - index + 1));
                func(s, i + 1, path, res);
                path.pop_back();

            }


        }
    }




    bool is_pal(string s, int start, int end) {

        while (start <= end) {
            if (s[start++] != s[end--]) {
                return false;
            }
        }
        return true;

    }
};


