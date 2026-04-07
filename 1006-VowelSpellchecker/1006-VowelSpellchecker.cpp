// Last updated: 07/04/2026, 11:37:26
class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> exact(wordlist.begin(), wordlist.end());
        unordered_map<string, string> capital;
        unordered_map<string, string> vowel;

        // lowercase function
        auto toLower = [&](const string &s) {
            string res = s;
            for (auto &c : res) c = tolower((unsigned char)c);
            return res;
        };

        // replace vowels with '*'
        auto vErr = [&](const string &s) {
            string res = s;
            for (auto &c : res) {
                c = tolower((unsigned char)c);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') 
                    c = '*';
            }
            return res;
        };

        // build maps (capital-insensitive and vowel-error-insensitive)
        for (auto &word : wordlist) {
            string lower = toLower(word);
            string vwl = vErr(word);
            capital.emplace(lower, word);  // only first occurrence kept
            vowel.emplace(vwl, word);      // only first occurrence kept
        }

        // process queries
        vector<string> ans;
        for (auto &query : queries) {
            if (exact.count(query)) {
                ans.push_back(query); // exact match
            } else {
                string lower = toLower(query);
                string vwl = vErr(query);
                if (capital.count(lower)) ans.push_back(capital[lower]);
                else if (vowel.count(vwl)) ans.push_back(vowel[vwl]);
                else ans.push_back(""); // no match
            }
        }

        return ans;
    }
};
