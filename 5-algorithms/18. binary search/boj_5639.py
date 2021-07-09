import sys
sys.getrecursionlimit(10**6)

class Node:
    def __init__(self, k, p):
        self.left = None
        self.right = None
        self.value = k
        self.parent = p


def preorder_input(k, parent):

    try:
        val = int(sys.stdin.readline())
    except:
        return

    if val < k:
        parent.left = Node(val, parent)
        preorder_input(val, parent.left)
    elif val > k:
        if parent.parent.parent is not None:
            if head.value < val:
                parent.right = Node(val, parent.right)
                preorder_input(val, parent.parent)
            else:
                parent.parent.right = Node(val, parent.parent)
                preorder_input(val, parent.parent)
        else:
            parent.parent.right = Node(val, parent.parent)
            preorder_input(val, parent.parent.right)
    return


def print_postorder(parent):
    if parent is None:
        return
    print_postorder(parent.left)
    print_postorder(parent.right)
    print(parent.value)
    return


head = Node(int(sys.stdin.readline()), None)

if __name__ == '__main__':

    preorder_input(head.value, head)
    print_postorder(head)
