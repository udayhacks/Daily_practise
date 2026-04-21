// Last updated: 21/04/2026, 17:39:53
1/*
2// Definition for a Node.
3class Node {
4    public int val;
5    public List<Node> neighbors;
6    public Node() {
7        val = 0;
8        neighbors = new ArrayList<Node>();
9    }
10    public Node(int _val) {
11        val = _val;
12        neighbors = new ArrayList<Node>();
13    }
14    public Node(int _val, ArrayList<Node> _neighbors) {
15        val = _val;
16        neighbors = _neighbors;
17    }
18}
19*/
20
21class Solution {
22    public Node cloneGraph(Node node) {
23
24        HashMap <Node , Node> map = new HashMap<>(); // map store clone node and reused 
25        // map is also a visited array ;
26
27        Queue<Node > que = new LinkedList<>();
28
29
30        if ( node == null) return null;
31        map.put(node, new Node(node.val));
32
33
34        que.offer(node);
35
36        while( !que.isEmpty()){
37
38            Node cur = que.poll();
39            
40            for ( Node n : cur.neighbors){
41                if( !map.containsKey(n)){ // if  till now n node doesn't have clone node;
42                    map.put(n, new Node(n.val));
43                    que.offer(n);
44                }
45
46                map.get(cur).neighbors.add(map.get(n));
47
48            }
49
50
51
52
53
54
55        }
56
57        return map.get(node);
58
59
60
61    }
62}