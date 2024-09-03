""" Formatted Strings """
'''
* Formatted Strings are particular useful in situations where we dynamically generate some text with our veriables. 

* '{}' -> with these curly braces, we're defining place holders or holds our string, and we run our program these holds will be filled with the value of our variables.

* f-string -> f'{}' -> f-string is a string literal that allows embedded expressions. This is useful when you want to include the value of a variable inside a string. f-string is prefixer.
'''

first = 'John'
last = 'Smith'
massage = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)
