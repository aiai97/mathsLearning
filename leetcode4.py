# I know I am fragile like a vase or glass and sometimes coding can be intimidating and docs can be so lengthy and so tedious and I always cry.
# But I always tell myself that don't despair and that I need to learn to enjoy the fun of programming.
# Anyway,I wanna be a smart software engineer and data scientist.
# class ListNode:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
# one = ListNode(1)
# two = ListNode(2)
# three = ListNode(3)
# one.next = two
# two.next = three
# head = one

# print(head.val)
# print(head.next.val)
# print(head.next.next.val)

# ptr = head
# head = head.next
# head = None


# def get_sum(head):
#     ans = 0
#     while head:
#         ans += head.val
#         head = head.next
#
#     return ans

#Traversal
# def get_sum(head):
#     ans = 0
#     while head:
#         ans += head.val
#         head = head.next
#     return ans
#recursively
# def get_sum(head):
#     if not head:
#         return 0
#     return head.val + get_sum(head.next)
# result = get_sum(head)
# print(result)
# class ListNode:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# Let prev_node be the Node at position i-1
# 1->2->3  add 4
# 1->2->3  1->2->4
# 1->2->4->3
# Singly linked list
# add a new node
# Let prev_node be the node at position i - 1
# def add_node(prev_node,node_to_add):
#     node_to_add.next = prev_node.next
#     prev_node.next = node_to_add
# delete the element at position i
# Let prev_node be the node at position i - 1
# def delete_node(prev_node):
#     prev_node.next = prev_node.next.next
# Doubly linked list
# class ListNode:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#         self.prev = None

#Let node be the node at position i
# def add_node(node,node_to_add):
# Let node be the node at position i
#  1 <-> node 3 <-> 4  add 2 at index 1
#  initialization prev_node 1 <-(param node) 3
# node_to_add 2 -> node 3  pre_node 1 <- node_to_add 2
# that is to say 2 -> 3  1 <- 2
#  prev_node 1 —> node_to_add 2   node_to_add 2 <- node 3
# that is to say 1 -> 2  2 <- 3
# the node represents the location or index where I wanna make a modification to the linkedlist
# node_to_add represents the node element which have two properties: value and its reference to the next node
# question: why we need to find prev_node at first?
# answer: imagine we are in a new env,we need to know the prev and latter person,then we can find our location.
# we need to show your initiative at first then we can make connections.
# def add_node(node,node_to_add):
#     prev_node = node.prev
#     node_to_add.next = node
#     node_to_add.prev = prev_node
#     prev_node.next = node_to_add
#     node.prev = node_to_add

# Let node be the node at position i
# 1 <-> 2 <-> 3 <-> 4  I am gonna remove element at index 1,that is 2 in the linkedlist
# initilization: prev_node 1 <->  (param node) 2 <->next_node 3 <-> 4
# prev_node 1 -> next_node 3   prev_node 1 <- next_node 3
# prev_node 1 <-> next_node 3 <-> 4
# 1 <-> 3 <-> 4
# hint: in doubly linkedlist, everytime I wanna manipulate an element at a random index,I must have a grasp of my neighbors
# def delete_node(node):
#     prev_node = node.prev
#     next_node = node.next
#     prev_node.next = next_node
#     next_node.prev = prev_node
# Linked lists with sentinel nodes
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# 1 <-> 2 <-> 3 <-> tail,I wanna add 4 at the end
# node_to_add 4 -> tail
# tail.prev 3  <- node_to_add 4
# that is, 3 <- 4 -> tail
# tail.prev 3 -> node_to_add 4
# node_to_add 4 <- tail
# that is, 3 -> 4 <- tail

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add


# 1 <-> 2 <-> 3 <-> 4 <-> tail, I wanna remove the end,that is 4
# find the end element that has value,that will be the node_to_remove,in this case,will be 4
# initialization: 1 <-> 2 <-> node_to_remove.prev 3 <-> node_to_remove 4 <-> tail
#  node_to_remove 4 <- tail
#  node_to_remove.prev.next 3 -> tail
#  3 <- tail
def remove_from_end():
    # if head.next == tail:: Checks if there are any nodes in the linked list.
    # If there are no nodes (i.e., the head.next points to the tail), it means the list is empty,
    # so there is nothing to remove. In this case, the function returns without performing any further actions.
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

# head <-> 1 <-> 2 <-> 3,I wanna add 0 at the beginning
# head <- node_to_add 0
# node_to_add 0 -> 1
# that is to say,  head <- 0 -> 1
# node_to_add 0 <- head.next.prev
#

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add


def remove_from_start():
    if head.next == tail:
        return

    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next


head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
