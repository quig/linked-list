import unittest
from LinkedList import LinkedList
from Node import Node


class TestStringMethods(unittest.TestCase):

    def test_if_I_am_able_to_display_my_linked_list(self):
        list = LinkedList(["1", "2", "3"])
        self.assertEqual("1->2->3->NULL", list.printList())

    def test_if_I_am_able_to_reverse_my_linked_list(self):
        list = LinkedList(["1", "2", "3"]).reverse()
        self.assertEqual("3->2->1->NULL", list.printList())



if __name__ == '__main__':
    unittest.main()
