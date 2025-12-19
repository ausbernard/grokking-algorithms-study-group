"""
Instructions:

To run these tests, open a terminal in this directory and execute:

    python test_linked_lists.py

Or, to see more detailed output:

    python -m unittest -v test_linked_lists.py

Make sure your implementation in 'linked_lists.py' is complete and saved before running the tests.
"""
import unittest
import unittest
from linked_lists import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_at_end(self):
        self.ll.insert_at_end(10)
        self.ll.insert_at_end(20)
        self.ll.insert_at_end(30)
        self.ll.insert_at_end(40)
        self.assertEqual(self.ll.Head.data, 10)
        self.assertEqual(self.ll.Head.next.data, 20)
        self.assertEqual(self.ll.Head.next.next.data, 30)
        self.assertEqual(self.ll.Head.next.next.next.data, 40)
        self.assertIsNone(self.ll.Head.next.next.next.next)

    def test_insert_at_position(self):
        self.ll.insert_at_end(10)
        self.ll.insert_at_end(20)
        self.ll.insert_at_end(30)
        self.ll.insert_at_end(40)
        self.ll.insert_at_position(1, 20)  # Insert at head
        self.assertEqual(self.ll.Head.data, 20)
        self.ll.insert_at_position(2, 30)  # Insert at position 2
        self.assertEqual(self.ll.Head.next.data, 30)
        self.ll.insert_at_position(3, 40)  # Insert at position 3
        self.assertEqual(self.ll.Head.next.next.data, 40)
        self.ll.insert_at_position(4, 50)  # Insert at position 4
        self.assertEqual(self.ll.Head.next.next.next.data, 50)

    def test_delete_any_position(self):
        self.ll.insert_at_end(10)
        self.ll.insert_at_end(20)
        self.ll.insert_at_end(30)
        self.ll.insert_at_end(40)
        self.ll.insert_at_position(1, 20)
        self.ll.insert_at_position(2, 30)
        self.ll.insert_at_position(3, 40)
        self.ll.insert_at_position(4, 50)
        self.ll.delete_any_position(4)
        # After deleting position 4, check the list
        current = self.ll.Head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        self.assertNotIn(50, values)

    def test_print_list(self):
        self.ll.insert_at_end(10)
        self.ll.insert_at_end(20)
        self.ll.insert_at_end(30)
        self.ll.insert_at_end(40)
        # Just check that print_list does not raise
        try:
            self.ll.print_list()
        except Exception as e:
            self.fail(f"print_list() raised {e}")

    def test_head_values(self):
        self.ll.insert_at_end(10)
        self.ll.insert_at_end(20)
        self.ll.insert_at_end(30)
        self.ll.insert_at_end(40)
        self.assertEqual(self.ll.Head.data, 10)
        self.assertEqual(self.ll.Head.next.data, 20)
        self.assertEqual(self.ll.Head.next.next.data, 30)
        self.assertEqual(self.ll.Head.next.next.next.data, 40)

if __name__ == "__main__":
    unittest.main()
