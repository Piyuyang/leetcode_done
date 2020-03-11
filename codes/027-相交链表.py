"""
编写一个程序，找到两个单链表相交的起始节点。
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    # 法一，暴力，超出时间限制
    # nodeA = headA
    # nodeB = headB
    # while nodeA:
    #     while nodeB:
    #         if nodeB is nodeA:
    #             return nodeB
    #         else:
    #             nodeB = nodeB.next
    #     nodeA = nodeA.next
    #     nodeB = headB

    # 法一改进
    headA_id = {}
    while headA:
        headA_id[id(headA)] = 1
        headA = headA.next
    while headB:
        if id(headB) in headA_id:
            return headB
        headB = headB.next


if __name__ == '__main__':
    listA = [4, 1, 8, 4, 5]
    listB = [5, 0, 1]
    nodeA = []
    nodeB = []
    for i in listA:
        nodeA.append(ListNode(i))
    for j in listB:
        nodeB.append(ListNode(j))
    nodeB.extend(nodeA[2:])

    i, j = 0, 0
    while i < len(nodeA) - 1:
        nodeA[i].next = nodeA[i + 1]
        i += 1
    while j < len(nodeB) - 1:
        nodeB[j].next = nodeB[j + 1]
        j += 1

    print(getIntersectionNode(nodeA[0], nodeB[0]))
