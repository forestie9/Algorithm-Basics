# Code from GeeksforGeeks website
# Python code to demonstrate the working of 
# array(), append(), insert()
  
# importing "array" for array operations
import array
  
# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3]) 
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,3):
    print (arr[i], end=" ")
 
print ("\r")
 
# using append() to insert new value at end
arr.append(4);
 
# printing appended array
print ("The appended array is : ", end="")
for i in range (0, 4):
    print (arr[i], end=" ")
     
# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)
 
print("\r")
 
# printing array after insertion
print ("The array after insertion is : ", end="")
for i in range (0, 5):
    print (arr[i], end=" ")

# Output:
# The new created array is : 1 2 3 
# The appended array is : 1 2 3 4 
# The array after insertion is : 1 2 5 3 4 

# -------------------------------------------------------------------------
# Python code to demonstrate the working of 
# pop() and remove()
  
# importing "array" for array operations
import array
  
# initializing array with array values
# initializes array with signed integers
arr= array.array('i',[1, 2, 3, 1, 5]) 
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
 
print ("\r")
 
# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2));
 
# printing array after popping
print ("The array after popping is : ",end="")
for i in range (0,4):
    print (arr[i],end=" ")
 
print("\r")
 
# using remove() to remove 1st occurrence of 1
arr.remove(1)
 
# printing array after removing
print ("The array after removing is : ",end="")
for i in range (0,3):
    print (arr[i],end=" ")
# Output:
# The new created array is : 1 2 3 1 5 
# The popped element is : 3
# The array after popping is : 1 2 1 5 
# The array after removing is : 2 1 5 

# -------------------------------------------------------------------------
# Python code to demonstrate the working of 
# index() and reverse()
  
# importing "array" for array operations
import array
  
# initializing array with array values
# initializes array with signed integers
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")
 
print ("\r")
 
# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2 is : ",end="")
print (arr.index(2))
 
#using reverse() to reverse the array
arr.reverse()
 
# printing array after reversing
print ("The array after reversing is : ",end="")
for i in range (0,6):
print (arr[i],end=" ")
# Output:
# The new created array is : 1 2 3 1 2 5 
# The index of 1st occurrence of 2 is : 1
# The array after reversing is : 5 2 1 3 2 1


############################################################################### -------------------------------------------------------------------------
# Search, insert and delete in an unsorted array

# Python program for searching in
# unsorted array 
def findElement(arr, n, key):
    for i in range (n):
        if (arr[i] == key):
            return i
    return -1
  
arr = [12, 34, 10, 6, 40]
key = 40
n = len(arr)
  
#search operation
index = findElement(arr, n, key)
if index != -1:
    print ("element found at position: " + str(index + 1 )) 
else:
    print ("element not found")

# Output:
# Element Found at Position: 5
# Time complexity: O(n)

# -------------------------------------------------------------------------
# Python program for inserting
# an element in an unsorted array
 
# method to insert element
def insert(arr, element):
    arr.append(element)
 
# declaring array and key to insert 
arr = [12, 16, 20, 40, 50, 70]
key = 26
  
# array before inserting an element
print ("Before Inserting: ")
print (arr)
  
# array after Inserting element 
insert(arr, key)
print("After Inserting: ")
print (arr)	

# Output:
# Before Insertion: 12 16 20 40 50 70 
# After Insertion: 12 16 20 40 50 70 26
# Time complexity: O(1)
	
# -------------------------------------------------------------------------	
# Python program to delete an element
# from an unsorted array
# In delete operation, the element to be deleted is searched 
# using the linear search and then delete operation is performed followed by shifting the elements.
 
# Declaring array and key to delete
arr = [10, 50, 30, 40, 20]
key = 30
  
print("Array before dletion:")
print arr
  
# deletes key if found in the array 
# otherwise shows error not in list
arr.remove(key)
print("Array after deletion")
print(arr)

# Output:
# Array before deletion
# 10 50 30 40 20 
# Array after deletion
# 10 50 40 20 
# Time complexity: O(n)

############################################################################### -------------------------------------------------------------------------
# Search, insert and delete in a sorted array

# python 3  program to implement binary search in sorted array
 
def binarySearch(arr, low, high, key):
 
    if (high < low):
        return -1
    # low + (high - low)/2
    mid = (low + high)/2
 
    if (key == arr[int(mid)]):
        return mid
 
    if (key > arr[int(mid)]):
        return binarySearch(arr,
           (mid + 1), high, key)
 
    return (binarySearch(arr, low,
           (mid -1), key))
 
# Driver program to check above functions 
# Let us search 10 in below array
arr = [5, 6, 7, 8, 9, 10]
n = len(arr)
key =10
print("Index:", int(binarySearch(arr,0, n, key) ))
# Output:
# Index: 5
# Time complexity: O(Log(n)): using Binary Search

# Insert Time complexity: O(n): in worst case all elements may have to be removed
# Delete Time complexity: O(n): in worst case all elements may have to be removed









