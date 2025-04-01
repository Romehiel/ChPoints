da_list = ['Arthur','Eleanor','Amir','Leticia', 'Quincy']
thy_tuple = ('Kaya', 'Velimir', 'Minerva', 'Flare', 'Lizzie')
it_float = 1.999
ze_int = 30
from decimal import Decimal
la_decimal = Decimal (10.24614442)
# print(la_decimal)
# 10.24614442000000025245753931812942028045654296875
the_dic = {'Cell':'Potato', 'Forma':'Cheese', 'Exilus':'Tomato', 'Kuva':'Pepper'}



# Exercise 2: Round your float up.

import math
exercise_2 = math.ceil(it_float)
print(exercise_2)

# Exercise 3: Get the square root of your float.

exercise_3 = math.sqrt(it_float)
print(exercise_3)

# Exercise 4: Select the first element from your dictionary.

exercise_4key = next(iter(the_dic))
exercise_4value = the_dic[exercise_4key]
print(f"First element: {exercise_4key}, First value: {exercise_4value}")

# Exercise 5: Select the second element from your tuple.

exercise_5 = thy_tuple[1]
print(exercise_5)

# Exercise 6: Add an element to the end of your list.

da_list.append('Aoi')
print(da_list)

# Exercise 7: Replace the first element in your list.
da_list[0] = 'Excalibur'
print(da_list)

# Exercise 8: Sort your list alphabetically.

da_list.sort()
print(da_list)

# Exercise 9: Use reassignment to add an element to your tuple.

thy_tuple  += ('Neci',)
print(thy_tuple)
