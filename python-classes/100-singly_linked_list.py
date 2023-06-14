#!/usr/bin/python3
"""Defines a class Node"""



class Node:
    """Defines a node of a singly linked list
    Args:
        data (int): The data inside the node
        next_node (Node): The next node
    """
    def __init__(self, data, next_node=None):
        """Instantiates a linked list node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the value inside a node
        Returns:
            The value inside the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data inside a node
        Args:
            value (int): the value to set
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")
    @property
    def next_node(self)
        """Returns the next node
        Returns:
            The next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets a the next node of this node
        Args:
            value (Node): The next node
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
class SinglyLinkedList:
    def __init__(self):
        """Simple instantation, sets the head to None"""
        self.__head = None

    def __str__(self):
        """Returns the string to print
        Returns:
            A string to print
        """
        retstr = ""
        tmp = self.__head
        while tmp is not None:
            retstr += (str(tmp.data) + "\n")
            tmp = tmp.next_node
        return retstr

    def sorted_insert(self, value):
        """Inserts a node inside the list with the correct sorted position
        (increasing order)
        Args:
            value (int): The value of the new node
        """
        new_node = Node(value)
        tmp = self.__head
        if tmp == None:
            self.__head = new_node
            return

        while tmp.next_node is not None and tmp.data < value:
            tmp = tmp.next_node
        new_node.next_node = tmp.next_node
        tmp.next_node = new_node
