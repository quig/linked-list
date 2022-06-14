from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def __init__(self, list):
        self.head = None
        for i in range(len(list)):
            self.push(list[i])

    def push(self, data):
        if self.head is None:
            self.head = Node(data=data)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data=data)

    def reverse(self):
        previous_node, current_node, following_node = None, self.head, None

        while current_node is not None:
            following_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = following_node

        # we reached the end here, we assign the new head
        self.head = previous_node
        return self

    def printList(self):
        textToDisplay = ""
        current_node = self.head

        while current_node is not None:
            if current_node == self.head:
                textToDisplay += current_node.data
            else:
                textToDisplay += "->" + current_node.data
            current_node = current_node.next
        if current_node == self.head:
            textToDisplay += "NULL"
        else:
            textToDisplay += "->NULL"

        return textToDisplay
