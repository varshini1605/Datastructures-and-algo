'''Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.'''

'''index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
remove():- This function removes the first occurrence of the value mentioned in arguments.
count():- This function counts the number of occurrences of value mentioned in arguments.'''

from collections import deque 
     
# Declaring deque 
queue = deque(['name','age','DOB'])  
#queue.append('class') 
queue.appendleft('class')   
print(queue)
#queue.popleft()
#print(queue)
queue.insert(1,3)
print(queue.count('name'))
print(queue)