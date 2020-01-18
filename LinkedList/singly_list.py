class Node:
	"""docstring for ClassName"""
	def __init__(self, value):
		self.value = value
		self.next = None

	def get_data(self):
		return self.value

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next


class LinkedList:
	"""docstring for ClassName"""
	def __init__(self):
		self.head = None


	def push(self, value):
		new_node = Node(value)
		if self.head:
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = new_node

		return self.head


	def size(self):
		count=0
		current_node = self.head
		while current_node:
			count = count + 1
			current_node = current_node.next

		return count


	def display_items(self):
		current_node = self.head
		while current_node:
			print(current_node.value),
			current_node = current_node.next

		print

	def search(self, value):
		current_node = self.head
		found = False
		while current_node:
			if current_node.value == value:
				found = True
				break
			else:
				current_node = current_node.next

		if current_node is None:
			raise ValueError("Data not found")

		return current_node

	def resursive_search(self, head, value):
		" return true if value present else return false "
		if not head:
			return False
		
		if head.value == value:
			return True

		else:
			return self.resursive_search(head.next, value)

	def delete(self, value):
		current_node = self.head
		previous_node = None

		found = False

		while current_node and not found:
			if current_node.value == value:
				found = True
				break
			else:
				previous_node = current_node
				current_node = current_node.next

		if current_node is None:
			raise ValueError("Data not found")

		if previous_node is None:
			self.head = current_node.get_next()
		else:
			previous_node.set_next(current_node.get_next())

		return self.head


	def nth_node_from_end_approach1(self, n):
		# count lenth of list, then return len-n+1'th node
		list_sz = self.size()
		if n>list_sz:
			raise ValueError("Index out of bounds")
		counter = 0
		current_node = self.head

		while counter<list_sz-n:
			current_node = current_node.next
			counter = counter + 1

		return current_node.value


	def nth_node_from_end_approach2(self, n):
		#  Using two pointers 1,2,3,4,5
		node1 = self.head
		node2 = self.head

		while n>0 and node1:
			node1 = node1.next
			n = n-1

		if n>0:
			raise ValueError("Index out of bounds")


		while node1:
			node2 = node2.next
			node1 = node1.next

		return node2.value



	def nth_node_from_end(self, n, approach_type=1):
		if approach_type == 1:
			return self.nth_node_from_end_approach1(n)
		if approach_type == 2:
			return self.nth_node_from_end_approach2(n)


	def find_middle_node(self):
		if not self.head or not self.head.next:
			return self.head
		
		slow_pointer = self.head
		fast_pointer = self.head

		while fast_pointer and fast_pointer.next:
			slow_pointer = slow_pointer.next
			fast_pointer = fast_pointer.next.next

		return slow_pointer.value



list = LinkedList()
list.push(5)
list.push(4)
list.push(1)
list.push(6)
# list.push(7)
list.display_items()
# print(list.resursive_search(list.head, 1))
# print(list.search(6).value)

# list.delete(6)

# list.display_items()

# list.delete(6)

# print(list.nth_node_from_end(1, approach_type=1))
# print(list.nth_node_from_end(1, approach_type=2))

print(list.find_middle_node())

		