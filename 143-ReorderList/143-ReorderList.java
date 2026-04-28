// Last updated: 28/04/2026, 09:26:17
1class Solution {
2
3    ListNode midPoint(ListNode head) {
4
5        ListNode slow = head;
6        ListNode fast = head;
7
8        while (fast.next != null && fast.next.next != null) {
9            fast = fast.next.next;
10            slow = slow.next;
11        }
12
13        return slow;
14    }
15
16    ListNode reverse(ListNode head) {
17
18        ListNode prev = null;
19        ListNode cur = head;
20
21        while (cur != null) {
22
23            ListNode next = cur.next;
24            cur.next = prev;
25            prev = cur;
26            cur = next;
27        }
28
29        return prev;
30    }
31
32    void merge(ListNode first, ListNode second) {
33
34        while (second != null) {
35
36            ListNode temp1 = first.next;
37            ListNode temp2 = second.next;
38
39            first.next = second;
40            second.next = temp1;
41
42            first = temp1;
43            second = temp2;
44        }
45    }
46
47    public void reorderList(ListNode head) {
48
49        if (head == null || head.next == null)
50            return;
51
52        ListNode midNode = midPoint(head);
53
54        ListNode secondHalf = midNode.next;
55        midNode.next = null;
56
57        ListNode secondHalfReverse = reverse(secondHalf);
58
59        merge(head, secondHalfReverse);
60    }
61}