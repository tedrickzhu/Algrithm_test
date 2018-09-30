# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def addTwoNumbers(self, l1, l2):
		lna = l1
		lnb = l2
		head = None
		result = None
		extence = 0

		while 1:
			sumab = lna.val + lnb.val + extence
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
		return head


def stringToIntegerList(input):
	return json.loads(input)


def stringToListNode(input):
	# Generate list from the input
	numbers = stringToIntegerList(input)

	# Now convert that list into linked list
	dummyRoot = ListNode(0)
	ptr = dummyRoot
	for number in numbers:
		ptr.next = ListNode(number)
		ptr = ptr.next

	ptr = dummyRoot.next
	return ptr


def listNodeToString(node):
	if not node:
		return "[]"

	result = ""
	while node:
		result += str(node.val) + ", "
		node = node.next
	return "[" + result[:-2] + "]"


def main():
	import sys
	def readlines():
		for line in sys.stdin:
			yield line.strip('\n')

	lines = readlines()
	while True:
		try:
			line = next(lines)
			l1 = stringToListNode(line);
			line = next(lines)
			l2 = stringToListNode(line);

			ret = Solution().addTwoNumbers(l1, l2)

			out = listNodeToString(ret);
			print(out)
		except StopIteration:
			break


if __name__ == '__main__':
	main()