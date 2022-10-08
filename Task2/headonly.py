class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None


def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
head = Node('1')
head=hasCycle(head)



