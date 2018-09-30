#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午7:16
# @Author  : zhuzhengyi
# @File    : isLOOP.py
# @Software: PyCharm
'''
Is it a loop ? （判断链表是否有环？）

Assume that we have a head pointer to a link-list. Also assume that we know the list is single-linked.
Can you come up an algorithm to check whether this link list includes a loop by using O(n) time and O(1) space
where n is the length of the list? Furthermore,can you do so with O(n) time and only one register?

方法：使用两个指针，从头开始，一个一次前进一个节点，一个前进2个节点；
如果无环，则最多2N，后两个指针可以重合，则正常停止。
如果单步前进的指针移动了N次之后依然未重合，则 说明有环

同样的，可以找到链表的中间节点。同上。

同样，利用此思想找到中间节点后可以较快的找到链表中倒数第m个元素
'''