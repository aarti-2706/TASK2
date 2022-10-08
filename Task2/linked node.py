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


head = Node('3')
node1 = Node('2')
node2 = Node('0')
node3 = Node('-4')


head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

head=detectCycle(head)
print(head.data)
