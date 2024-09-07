""" If Statements """
'''
Simple Question -> 
Price of a house is $1M
if the buyer has good credit,
    they need to putdown 10%
Otherwise
    they need to putdown 20%
print the down payment
'''
# is_hot = False
# is_cold = False
# if is_hot:
#     print("It is a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It is cold day")
#     print("Wear warm clothes")
# else:
#     print("it is a lovely day")
# print("Enjoy your day")

# Solution ->

price_of_house = 1000000
is_good_credit = True
if is_good_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house
print(f"Down payment: ${down_payment}")