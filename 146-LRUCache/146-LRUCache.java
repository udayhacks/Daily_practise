// Last updated: 08/04/2026, 12:47:39
1import java.util.*;
2
3class LRUCache {
4
5    private final int capacity;
6    private LinkedHashMap<Integer, Integer> map;
7
8    public LRUCache(int capacity) {
9
10        this.capacity = capacity;
11
12        map = new LinkedHashMap<Integer, Integer>(
13            capacity, 0.75f, true
14        ) {
15            protected boolean removeEldestEntry(
16                Map.Entry<Integer, Integer> eldest
17            ) {
18                return size() > capacity;
19            }
20        };
21    }
22
23    public int get(int key) {
24        return map.getOrDefault(key, -1);
25    }
26
27    public void put(int key, int value) {
28        map.put(key, value);
29    }
30}