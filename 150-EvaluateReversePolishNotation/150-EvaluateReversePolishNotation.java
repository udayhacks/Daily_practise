// Last updated: 01/05/2026, 14:03:12
1class Solution {
2
3    private Stack<String> store;
4    private boolean isOperand (String s){
5
6        if ( s.equals("+") || s.equals("/") ||
7        s.equals("*") ||s.equals("-") ) return true;
8        return false;
9    }
10    private String operation(String a , String b, String s){
11        
12        if (  s.equals("+")) return Integer.toString(
13            Integer.parseInt(a)+Integer.parseInt(b)
14        );
15         else if (  s.equals("-")) return Integer.toString(
16            Integer.parseInt(a)-Integer.parseInt(b)
17        );
18         else if (  s.equals("/")) return Integer.toString(
19            Integer.parseInt(a)/Integer.parseInt(b)
20        );
21        else{  return Integer.toString(
22            Integer.parseInt(a)*Integer.parseInt(b)
23        );}
24
25        
26        
27    }
28
29    
30    public int evalRPN(String[] tokens) {
31
32        store = new Stack<>();
33
34        for (String token : tokens){
35            if ( isOperand(token)){
36                String a = store.pop();
37                String b = store.pop();
38                // b goes first into stack;
39                String res = operation(b,a,token);
40                store.push(res);
41            }else{
42                store.push(token);
43            }
44        }
45
46        return Integer.parseInt(store.peek());
47        
48        
49
50    }
51}