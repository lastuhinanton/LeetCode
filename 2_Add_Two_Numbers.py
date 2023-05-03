class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def fill_list(ownlist, idx):
    ownnode = None
    if idx != len(ownlist):
        ownnode = ListNode(ownlist[idx], fill_list(ownlist, idx+1))
    return ownnode

def print_list(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

first = [2,4,9]
second = [5,6,4,9]

f_node = fill_list(first, 0)
s_node = fill_list(second, 0)

def create_num(buf, mylist):
    if mylist:
        buf.append(str(mylist.val))
        create_num(buf, mylist.next)
    return int(''.join(buf[::-1]))

def ret_list(node, num):
    if num == 0: return None
    node = ListNode()
    node.val = num % 10
    node.next = ret_list(None, num // 10)
    return node

def addTwoNumbers(l1, l2):
    print(create_num(list(), l1))
    print(create_num(list(), l2))
    num = create_num(list(), l1) + create_num(list(), l2)
    print(num)
    ret = ret_list(None, num)
    if not ret: ret = ListNode()
    return ret

print_list(addTwoNumbers(f_node, s_node))

