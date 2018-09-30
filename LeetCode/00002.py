
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

ln1 = ListNode(2)
ln1.next = ListNode(4)
ln1.next.next = ListNode(3)

ln2 = ListNode(5)
ln2.next = ListNode(6)
ln2.next.next = ListNode(4)

lna = ln1
lnb = ln2
head = None
result = None
extence = 0

while 1:
	sumab = lna.val +lnb.val+ extence
	if sumab >= 10:
		sumab = sumab - 10
		extence = 1
	else:
		extence = 0
	if head is None:
		head = ListNode(sumab)
		result = head
	else:
		result.next = ListNode(sumab)
		result = result.next
	if lna.next is not None and lnb.next is not None:
		lna = lna.next
		lnb = lnb.next
	elif lna.next is None and lnb.next is not None:
		sumab = lnb.val + extence
		if sumab >= 10:
			sumab = sumab - 10
			extence = 1
		else:
			extence = 0
		if head is None:
			head = ListNode(sumab)
			result = head
		else:
			result.next = ListNode(sumab)
			result = result.next
	elif lna.next is not None and lnb.next is None:
		sumab = lna.val + extence
		if sumab >= 10:
			sumab = sumab - 10
			extence = 1
		else:
			extence = 0
		if head is None:
			head = ListNode(sumab)
			result = head
		else:
			result.next = ListNode(sumab)
			result = result.next
	elif lna.next is None and lnb.next is None:
		break
# print(head.next.val)
while 1 :
	print(head.val)
	if head.next is None:
		break
	head = head.next





l1 = [2,4,3]
l2 = [5,6,4]
result = []
len1 = len(l1)
len2 = len(l2)

if len1 >= len2:
	extence = 0
	for i in range(len2):
		a = l1[i]
		b = l2[i]
		sumab = a+b+extence
		if sumab >=10:
			sumab = sumab - 10
			extence = 1
		else:
			extence = 0
		result.append(sumab)
	if len1 > len2:
		for j in range(len2,len1):
			sumnew = l1[j]+extence
			if sumnew>=10:
				sumnew = sumnew - 10
				extence = 1
			else:
				extence = 0
			result.append(sumnew)
if len1<len2:
	extence = 0
	for i in range(len1):
		a = l1[i]
		b = l2[i]
		sumab = a + b + extence
		if sumab >= 10:
			sumab = sumab - 10
			extence = 1
		else:
			extence = 0
		result.append(sumab)
	for j in range(len1, len2):
		sumnew = l2[j] + extence
		if sumnew >= 10:
			sumnew = sumnew - 10
			extence = 1
		else:
			extence = 0
		result.append(sumnew)

print(result)
