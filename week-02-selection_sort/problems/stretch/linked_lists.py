"""
https://www.delftstack.com/howto/python/linked-list-in-python/
1. Create a Node class √
2. Create a Linked List class √
3. Create a def to print all elements of a linked list √
4. Create a def to insert an element at the beginning of a linked list
5. Create a def to insert an element at the end of a linked list
6. Create a def to insert an element at the middle of a linked list
7. Create a def to insert an element at any position of a linked list
8. Create a def to delete an element from a linked list
9. Create a def to count the elements in a linked list
9. Create a def to update a Node in a linked list

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.Head = None
    
    def print_list(self):
        pass
    
    def insert_into_empty_list(self, element):
        pass
    
    def insert_at_beginning(self, element):
        pass
        
    def insert_at_end(self, element):
        pass
            
    def insert_at_position(self, position, element):
        pass
    
    def delete_from_beginning(self):
        pass
    
    def delete_from_end(self):
        pass
    
    def delete_any_position(self, position):
        pass
                
            