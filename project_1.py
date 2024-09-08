""" Project: Weight Converter """
'''
* Input the wight by the user
* Choose the weight parameter like, (L)bs, (K)g
* Getting the output
'''
weight = int(input('Enter your weight: '))
unit = input('(L)bs or (K)g: ')
Lbs_to_Kg = weight * 0.45 
Kg_to_Lbs = weight / 0.45
if unit.upper() == 'L' and unit.lower() == 'l':
    print(f"You are {Lbs_to_Kg} kilos")
else:
    print(f"You are {Kg_to_Lbs} pounds")