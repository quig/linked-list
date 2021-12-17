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
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = Node(data=data)

    def reverse(self):
        currentNode = self.head
        while currentNode is not None:
            currentNode, currentNode.next = currentNode.next, currentNode
        return self

    def printList(self):
        textToDisplay = ""
        currentNode = self.head

        while currentNode is not None:
            if currentNode == self.head:
                textToDisplay += currentNode.data
            else:
                textToDisplay += "->" + currentNode.data
            currentNode = currentNode.next
        textToDisplay += "->NULL"

        return textToDisplay
