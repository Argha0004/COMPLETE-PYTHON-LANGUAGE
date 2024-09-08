""" Logical Operators """
'''
* in logical and operator, two condition should be true.
* in logical or operator, either only one must be true.
* in logcal not operator, we give it true boolean value it converts in to false.
'''

# has_high_income = False
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# has_good_credit = True
# has_criminal_records = False

# if has_good_credit and not has_criminal_records:
#     print("Eligible for loan")

print("----------------***--------------***----------------\n")

""" Comparison Operators """
'''
Simple Question ->
if name is less than 3 characters long
    name must be at least 3 characters
othewise if it's more than 50 characters long
    name can be maximum of 50 characters
otherwise
    name looks good!
'''
# Solution ->

name = input("You name is=> \n")
characters = len(name)
if characters < 3:
    print("Name must be at least 3 characters")
elif characters > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good!")