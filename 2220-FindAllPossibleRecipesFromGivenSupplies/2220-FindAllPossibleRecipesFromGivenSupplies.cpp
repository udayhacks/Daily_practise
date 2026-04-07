// Last updated: 07/04/2026, 11:35:14
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {

        unordered_map <string, int> req;
        unordered_map<string,vector<string>> graph;
        vector<string>ans ; 
        unordered_set <string> recipe(recipes.begin(),recipes.end());


            for (int i = 0; i < recipes.size(); i++) {
            for (string ingredient : ingredients[i]) {
                graph[ingredient].push_back(recipes[i]);
            }
            req[recipes[i]] = ingredients[i].size();
        }
        
        queue<string> que;
        for (string & sup:supplies){
            que.push(sup);
        }
            
       
       
     
      while(!(que.empty())){
        string front = que.front();
        que.pop();
        if (recipe.find(front) != recipe.end()){
            ans.push_back(front);
        }
        for (auto i : graph[front]){
            req[i]--;
            if (req[i] == 0 ) que.push(i);
        }
            }
        return ans;
        }
    };