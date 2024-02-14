'''extend(iterable):- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
extendleft(iterable):- This function is used to add multiple values at the left end of the deque. The argument passed is iterable. Order is reversed as a result of left appends.
reverse():- This function is used to reverse the order of deque elements.
rotate():- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.'''

from collections import deque 
queue = deque(['name','age','DOB'])
de = deque([1, 2, 3,])
de.extendleft([7,8,9])
print(de)
de.reverse()
print(de)
de.rotate(-3)
print(de)