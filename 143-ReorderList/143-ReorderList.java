// Last updated: 28/04/2026, 09:10:32
1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12
13    
14    public void reorderList(ListNode head) {
15
16
17        ListNode slow = head;
18        ListNode fast = head;
19
20
21        while( fast.next != null && fast.next.next != null){
22            fast = fast.next.next;
23            slow = slow.next;
24        }
25
26        ListNode second = slow.next;
27        ListNode prev = null ;
28        slow.next = null;
29
30
31        while( second != null){
32            
33            ListNode tmp = second.next;
34            second.next = prev;
35            prev = second;
36            second = tmp;
37
38        }
39
40        ListNode first = head;
41        second = prev;
42
43
44        while( second !=null){
45
46
47            ListNode firstNext = first.next;
48            ListNode secondNext = second.next;
49
50            first.next = second;
51            second.next = firstNext;
52
53            first = firstNext;
54            second = secondNext;
55        }
56
57
58
59
60
61
62
63    }
64}