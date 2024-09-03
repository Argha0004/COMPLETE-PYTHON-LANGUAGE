""" String """
'''
* we could use both '' and "" to define a string.
 
* [0] -> index refers always first word 'P' and negative index refers last value like [-1] -> refres 's'. 

* if we don't supply end index value, then python will return all the characters to the end of the string.

* if we don't supply first index value but add end index, the python interpreter will assume 0 as the start index.

* if we leave both the start index and the end index, now in this case [0] will be assumed as the start index, and the length of the end index will be string will assume at the end index. So with this systax, we can basically copy or a clone a string.
'''

course = 'Python for Beginners'
another = course[:]
print(another)

# Simple Solution --->>>
name = 'Jennifer'
print(name[1:-1]) # output -> ennife