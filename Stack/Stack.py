class Stack(object):
    """
    LIFO = Last In First Out
    """

    def __init__(self):
        self.items = []

    def push(self, elem):
        """
        Pushing element to end of Stack
        :param elem:
        :return: None
        """
        self.items.append(elem)
        pass

    def pop(self):
        """
        Removing the last element that was pushed (LIFO)
        :return: None
        """
        self.items.pop()
        pass

    def peek(self):
        """
        Checks end of Stack and returns last element if not empty
        :return: element at -1 index
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """
        Returns the length of Stack if not empty
        :return: Integer value
        """
        return len(self.items)

    def is_empty(self):
        """
        Checks if Stack is empty/not empty
        :return: True or False
        """
        if not self.items:
            return True
        else:
            return False


"""
Testing functionality
"""
my_Stack = Stack()
my_Stack.push("1")
my_Stack.push("4")
my_Stack.push("9")
my_Stack.push("16")
my_Stack.push("25")

print(my_Stack.peek())
my_Stack.pop()

print(my_Stack.peek())
print(my_Stack.size())
print(my_Stack.is_empty())

my_Stack.pop()
my_Stack.pop()
my_Stack.pop()

print(my_Stack.peek())
my_Stack.pop()

print(my_Stack.peek())
print(my_Stack.size())
print(my_Stack.is_empty())

