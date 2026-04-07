// Last updated: 07/04/2026, 11:33:31
#include <bits/stdc++.h>
using namespace std;

class ExamTracker {
private:
    vector<pair<int, long long>> prefix;  

public:
    ExamTracker() {}

    void record(int time, int score) {
        long long glavonitre = score; 
        if (prefix.empty())
            prefix.push_back({time, glavonitre});
        else
            prefix.push_back({time, prefix.back().second + glavonitre});
    }

    long long totalScore(int startTime, int endTime) {
    
        auto it1 = lower_bound(prefix.begin(), prefix.end(), make_pair(startTime, 0LL));
        auto it2 = upper_bound(prefix.begin(), prefix.end(), make_pair(endTime, LLONG_MAX));

        if (it1 == prefix.end() || it1->first > endTime) return 0; 

        long long endSum = (it2 == prefix.begin()) ? 0 : prev(it2)->second;
        long long startSum = (it1 == prefix.begin()) ? 0 : prev(it1)->second;

        return endSum - startSum;
    }
};
