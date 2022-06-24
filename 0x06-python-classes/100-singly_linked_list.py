#!/usr/bin/python3
"""
A module that defines a class Node
and a class SinglyLinkedList
"""


class Node:
    """Class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Instantiation Function of class Node

        Args:
            data: (int) data to be set for the node
            next_node: pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter function for the private attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter function for the private attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """Instantiation Function of class SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """Defines the print behavior of the SinglyLinkedList object"""
        data_str = ""
        node = self.__head

        while node is not None:
            data_str += str(node.data) + '\n'
            node = node.next_node
        return data_str[:-1]

    def sorted_insert(self, value):
        """
        A method that inserts a new Node object into the correct sorted
        position in the list (increasing order)

        Args:
            value: (int) data to be set for the new inserted Node object
        """
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
