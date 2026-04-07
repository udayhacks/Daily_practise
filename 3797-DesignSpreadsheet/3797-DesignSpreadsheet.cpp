// Last updated: 07/04/2026, 11:33:41
class Spreadsheet {
private:
int addition(string & val){
    if (map.count(val)) return map[val];
    if (isdigit(val[0]))return stoi(val);
    return 0;

}
public:
    unordered_map<string, int > map ;
    int row ;
    Spreadsheet(int rows) {
        this->row = rows;
    }
    
    void setCell(string cell, int value) {
        map[cell]  = value;
    }
    
    void resetCell(string cell) {
         map[cell]  = 0;
    }
    
    int getValue(string formula) {
        string expr = formula.substr(1);
        
        int plusIndex = expr.find('+');
        string left = expr.substr(0,plusIndex);
        string right = expr.substr(plusIndex+1);
        return addition(left)+addition(right);
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */