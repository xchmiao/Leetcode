## Problem: https://www.lintcode.com/problem/implement-three-stacks-by-single-array/description

class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.stack_size = size
        self.stack_pointer = [-1, -1, -1]
        self.index_used = 0
        self.buffer = [StackNode(-1, -1, -1) for _ in range(size*3)]

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        # Push value into stackNum stack
        last_index = self.stack_pointer[stackNum]
        self.stack_pointer[stackNum] = self.index_used
        self.index_used += 1
        self.buffer[self.stack_pointer[stackNum]] = StackNode(last_index, value, -1)
        if last_index != -1: # if it is not the 1st element in stack, linked to previous element (last)
            self.buffer[last_index].next = self.stack_pointer[stackNum]

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        # Pop and return the top element from stackNum stack
        value = self.buffer[self.stack_pointer[stackNum]].value
        last_index = self.stack_pointer[stackNum]
        if last_index != self.index_used - 1: # if the element is not the last element of list, exchange with the last one
            self.swap(last_index, self.index_used - 1, stackNum)
            
        self.stack_pointer[stackNum] = self.buffer[self.stack_pointer[stackNum]].prev # the stack_pointer set back to previous node, and last_index could be changed after the swap()
        if self.stack_pointer[stackNum] != -1: # not empt
            self.buffer[self.stack_pointer[stackNum]].next = -1
        
        self.buffer[self.index_used - 1] = None # remove the last node
        self.index_used -= 1 # reduce the index_used by 1
        return value
    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        # Return the top element
        return self.buffer[self.stack_pointer[stackNum]].value

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        # write your code here
        return self.stack_pointer[stackNum] == -1
    
    def swap(self, last_index, top_index, stackNum):
        if self.buffer[last_index].prev == top_index:
            self.buffer[last_index].value, self.buffer[top_index].value = self.buffer[top_index].value, self.buffer[last_index].value
            tp = self.buffer[top_index].prev # top's previous node
            if tp != -1:
                self.buffer[tp].next = last_index
            self.buffer[last_index].prev = tp
            self.buffer[last_index].next = top_index
            self.buffer[top_index].prev = last_index
            self.buffer[top_index].next = -1
            self.stack_pointer[stackNum] = top_index
            return
        
        lp = self.buffer[last_index].prev
        if lp != -1:
            self.buffer[lp].next = top_index
        
        tp = self.buffer[top_index].prev
        if tp != -1:
            self.buffer[tp].next = last_index
        
        tn = self.buffer[top_index].next
        if tn != -1:
            self.buffer[tn].prev = last_index
        else:
            for i in range(3):
                if self.stack_pointer[i] == top_index:
                    self.stack_pointer[i] = last_index
                    
        self.buffer[last_index], self.buffer[top_index] = self.buffer[top_index], self.buffer[last_index]
        self.stack_pointer[stackNum] = top_index

class StackNode:
    def __init__(self, prev, value, next):
        self.value = value
        self.prev = prev
        self.next = next
