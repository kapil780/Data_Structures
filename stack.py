class Stack(object):
    """docstring for Stack
    Creates a new stack on creating a class
    Functions:
    1.push_el = Put elements in stack. Takes one argument to be appended
    2.show_el = Show the stack
    3.pop_el = Remove top element from stack
    4.is_empty = Return true if stack is empty else return false 
"""

    def __init__(self):
        self.stack = []

    def push_el(self, element):
        self.stack.append(element)

    def show_el(self):
        print(self.stack)

    def pop_el(self):
        self.stack.pop()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


st = Stack()
b = Stack()
st.push_el(5)
st.push_el(20)
st.pop_el()
print(st.is_empty())
st.show_el()
