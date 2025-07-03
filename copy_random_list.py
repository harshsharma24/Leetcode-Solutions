class Node:
    self __init__(self, x, next=None,random=None):
        self.val=int(x)
        self.next=next
        self.random=random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur=head
        map={}

        while cur:
            copy=Node(cur.val)
            map[cur]= copy
            cur=cur.next

        cur=head
        while cur:
            copy.next= map.get(cur.next)
            copy.random=map.get(cur.random)
            cur= cur.next
        
        return map[head]


if __name__=="__main__":
    num=[[7,null],[13,0],[11,4],[10,2],[1,0]]
    copyRandomList()    
