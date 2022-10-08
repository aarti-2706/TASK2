class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None


def detectCycle(head):
    fast=head
    slow=head
    loopexist=0
    while(fast!=None and slow!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if(fast==slow):
            loopexist=1
            break

    if(loopexist):
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
    return None


head = Node('1')
node1 = Node('2')

head.next = node1
node1.next = head


head=detectCycle(head)
print(head.data)
