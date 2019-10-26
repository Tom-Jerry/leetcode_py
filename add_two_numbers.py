#-*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #创建一个头结点
        answer = ListNode(0)
        point = answer
        adding = 0
        while l1 or l2:

            #计算当前位的值，求余得出向高位的进位值之后，求余结果写入point指向的节点中
            #在answer中构造一个节点，来执行当前该位的计算
            point.next = ListNode(0)
            point = point.next

            #l1 l2均未走到尽头
            if l1 and l2:
                tmp = l1.val + l2.val + adding
                l1 = l1.next
                l2 = l2.next
            #l1走到尽头 l2未到
            elif l2:
                tmp = l2.val + adding
                l2 = l2.next
            #l2走到尽头 l1未到
            else:
                tmp = l1.val + adding
                l1 = l1.next
            #判断是否需要向高位进位，并将当前位的值写入point指向的节点
            if tmp < 10:
                point.val = tmp
                adding = 0
            else:
                point.val = tmp % 10
                adding = 1
        if adding == 1:
            point.next = ListNode(1)
        return answer.next
            