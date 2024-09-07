""" String Methods """
'''
Function and method definitions are different. 

print(), len() -> Functions

upper(), lower() -> Method in string, this are general

searching character's index values then use 'find()' method,

searching character's boolean expression then use 'in'
'''
course = "Python For Beginners"
# print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.find('s')) 
print(course.replace('Beginners', 'Students'))
print('Python' in course)
print(course.title())