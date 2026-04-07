# Last updated: 07/04/2026, 11:41:14
from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList :
            return 0 

        neig = defaultdict(list)
        # this dictionary contain all the pattern that wordlist make 
        # this a shortcut for making all possible combinations 
        # example : hit ---> h*t and *it and hi* 
        # dictionary all list of element that follow these like pattern and make it better

        for word in wordList:
            for j in range(len(word)) :
                pattern = word[:j] + "#" + word[j+1:]
                neig[pattern].append(word )

        level = 1
        que = deque()
        que.append(beginWord)
        visit = set(beginWord)
        # above i have create a set due to avoid revisiting 
        
        while que :



            for i in range(len(que)):
                word = que.popleft()
                # here am pop out the elment and checking whether it might be endword 
                #if so i can return the level
                if word == endWord : return level
                    # here we are doing the level while tranversal bfs like in tree to find level 
                for j in range(len(word)) :
                        pattern = word[:j] + "#" + word[j+1:]
                        # here add all unvisited elements into que by preparing the all neighbouring patterns
                        for ne in neig[pattern] :
                            if ne not in visit:
                                visit.add(ne)
                                que.append(ne)               

            level +=1
        return 0 