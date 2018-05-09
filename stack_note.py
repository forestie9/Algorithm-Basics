# stack

# push(), pop(), isEmpty() and peek() all take O(1) time.

# There are two ways to implement a stack:
# Using array
# Using linked list

# Python program for array implementation of stack
 
# import maxsize from sys module 
# Used to return -infinite when stack is empty
from sys import maxsize
 
# Function to create a stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack
 
# Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0
 
# Function to add an item to stack. It increases size by 1
def push(stack, item):
    stack.append(item)
    print("pushed to stack " + item)
     
# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) #return minus infinite
     
    return stack.pop()
 
# Driver program to test above functions    
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")

# 10 pushed to stack
# 20 pushed to stack
# 30 pushed to stack
# 30 popped from stack
# Top item is 20

#############################################################################
# Python program for linked list implementation of stack
# a) In push operation, if new nodes are inserted at the beginning of linked list, 
	# then in pop operation, nodes must be removed from beginning.
# b) In push operation, if new nodes are inserted at the end of linked list, 
	# then in pop operation, nodes must be removed from end. 
	
# Class to represent a node
class StackNode:
 
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data 
        self.next = None
 
class Stack:
     
    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None
 
    def isEmpty(self):
        return True if self.root is None else  False
 
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root 
        self.root = newNode
        print "%d pushed to stack" %(data)
     
    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root 
        self.root = self.root.next
        popped = temp.data
        return popped
     
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data
 
# Driver program to test above class 
stack = Stack()
stack.push(10)        
stack.push(20)
stack.push(30)
 
print "%d popped from stack" %(stack.pop())
print "Top element is %d " %(stack.peek())
 
# 10 pushed to stack
# 20 pushed to stack
# 30 pushed to stack
# 30 popped from stack
# Top element is 20

#############################################################################
# Binary representation of a given number
# Method 1: Iterative
# For any number, we can check whether its ‘i’th bit is 0(OFF) or 1(ON) by bitwise ANDing it with “2^i” (2 raise to i).

# void bin(unsigned n)
# {
    # unsigned i;
    # for (i = 1 << 31; i > 0; i = i / 2)
        # (n & i)? printf("1"): printf("0");
# }
 
# int main(void)
# {
    # bin(7);
    # printf("\n");
    # bin(4);
# }

# Method 2: Recursive
# step 1) if NUM > 1
	# a) push NUM on stack
	# b) recursively call function with 'NUM / 2'
# step 2)
	# a) pop NUM from stack, divide it by 2 and print it's remainder.

# void bin(unsigned n)
# {
    # /* step 1 */
    # if (n > 1)
        # bin(n/2);
 
    # /* step 2 */
    # printf("%d", n % 2);
# }
 
# int main(void)
# {
    # bin(7);
    # printf("\n");
    # bin(4);
# }

# Alternative pseudo code
# void fun(int n)
# {
    # Stack S;  // Say it creates an empty stack S
    # while (n > 0)
    # {
      # // This line pushes the value of n%2 to stack S
      # push(&S, n%2);
 
      # n = n/2;
    # }
 
    # // Run while Stack S is not empty
    # while (!isEmpty(&S))
      # printf("%d ", pop(&S)); // pop an element from S and print it
# }
	
# Check for balanced parentheses in an expression
from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))
# Time Complexity: O(n)
# Auxiliary Space: O(n) for stack.