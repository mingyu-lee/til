import unittest

class Node:

	def __init__(self, item):
		self.data = item
		self.next = None


class LinkedList:

	def __init__(self):
		self.nodeCount = 0
		self.head = Node(None)
		self.tail = None
		self.head.next = self.tail


	def __repr__(self):
		if self.nodeCount == 0:
			return 'LinkedList: empty'

		s = ''
		curr = self.head
		while curr.next:
			curr = curr.next
			s += repr(curr.data)
			if curr.next is not None:
				s += ' -> '
		return s


	def getLength(self):
		return self.nodeCount


	def traverse(self):
		result = []
		curr = self.head
		while curr.next:
			curr = curr.next
			result.append(curr.data)
		return result


	def getAt(self, pos):
		if pos < 0 or pos > self.nodeCount:
			return None
		print("getat pos", pos)
		i = 0
		curr = self.head
		while i < pos:
			print("curr", curr.data)
			print("curr.next", curr.next.data)
			curr = curr.next
			i += 1

		print("getat curr.data", curr.data)
		return curr


	def insertAfter(self, prev, newNode):
		newNode.next = prev.next
		if prev.next is None:
			self.tail = newNode
		prev.next = newNode
		self.nodeCount += 1
		return True


	def insertAt(self, pos, newNode):
		if pos < 1 or pos > self.nodeCount + 1:
			return False

		if pos != 1 and pos == self.nodeCount + 1:
			prev = self.tail
		else:
			prev = self.getAt(pos - 1)
		return self.insertAfter(prev, newNode)

	def popAfter(self, prev):
		print("prev.data", prev.data)
		if prev.next is None:
			return None
		if prev.next.next is None:
			print("prev.next", prev.next)
			tmp = prev.next
			prev.next = None
			self.tail = prev
		else:
			print("prev.next2", prev.next.data)
			tmp = prev.next
			print("prev.next.next", prev.next.next.data)
			prev.next = prev.next.next
		self.nodeCount -= 1
		return tmp.data

	def popAt(self, pos):
		if pos < 1 or pos > self.nodeCount:
			#raise IndexError
			return None
		print("popat pos", pos)
		return self.popAfter(self.getAt(pos-1))


	def concat(self, L):
		self.tail.next = L.head.next
		if L.tail:
			self.tail = L.tail
		self.nodeCount += L.nodeCount

class Test(unittest.TestCase):

	def test(self):
		list = [10, 2, 5, 1, 3]
		linkedList = LinkedList()

		for i, n in enumerate(list):
			linkedList.insertAt(i+1, Node(n))

		print(linkedList.popAt(1))
		print(linkedList.popAt(2))
		print(linkedList.popAt(3))
		print(linkedList.popAt(4))
		print(linkedList.popAt(5))

		# self.assertIsNone(linkedList.popAt(0))
		# self.assertEqual(linkedList.popAt(1), 10)
		# self.assertEqual(linkedList.popAt(2), 2)
		# self.assertEqual(linkedList.popAt(3), 5)
		# self.assertEqual(linkedList.popAt(4), 1)
		# self.assertEqual(linkedList.popAt(5), 3)
		# self.assertIsNone(linkedList.popAt(6))

		# linkedList = LinkedList()
		# list = []
		# for i, n in enumerate(list):
		# 	linkedList.insertAt(i+1, Node(n))

		# self.assertEqual(linkedList.popAt(1), None)

		# linkedList = LinkedList()
		# list = [99]
		# for i, n in enumerate(list):
		# 	linkedList.insertAt(i+1, Node(n))
		
		# self.assertEqual(linkedList.popAt(1), 99)

if __name__ == "__main__":
	unittest.main()
