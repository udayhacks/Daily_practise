// Last updated: 07/04/2026, 11:34:11
class Solution {
private:
bool isvowel(char c){
    char ch =tolower(c);
    return ch == 'a' || ch == 'e'|| ch ==  'i'|| ch =='o'|| ch == 'u';
}
public:
    bool isValid(string word) {
        
        if (word.size()<3){
            return false;
        }
        bool vol = false, cons = false; 
        for (auto ch :word){
            if (!isalnum(ch)){
                return false;
            }
            if (isalpha(ch)){
                if (isvowel(ch)){
                    vol = true;
                }
                else{
                    cons = true;
                }
            }
        
        }
        return vol && cons;


    }
};