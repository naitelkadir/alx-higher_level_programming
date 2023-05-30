#!/usr/bin/python3
""" Define a new node"""
class Node:
    """Represent the node"""
    def __init__(self, data, next_node=None):
        """Initialize the node
        Args:
            data(int): the data of the node
            next_node(Node): next node
        """
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        """ proprety to retrieve the datat"""
        return (self.__data)
    @data.setter
    def data(self, value):
        """ to set the data to a value"""
        self.__data = value
        if not type(value) is int:
            raise TypeError("data must be an integer")
    @property
    def next_node(self):
        """property to retrieve the next node """
        return (self.__next_node)
    @next_node.setter
    def next_node(self, value):
        """property to set the next node to a value"""
        self.__next_node = value
        if value != None and not type(value) is Node:
            raise TypeError("next_node must be a Node object")
"""Define a new singly linkedlist"""
class SinglyLinkedList:
    """Represent the singly linked list"""
    def __init__(self):
        """Initialize the list
        Args:
            head: ...
        """
        self.__head = None
    def sorted_insert(self, value):
        """ method to insert end sort the list
        Args:
            value (Node): the data to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
    def __str__(self):
        """to print to stdout"""
        tmp = self.__head
        values = []
        while (tmp is not None):
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))
