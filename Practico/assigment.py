cool_string = 'The conclave'
nice_number = 77
sick_list = ['Alpharius', 'Betalamine', 'Gammacor', 'Omegalul', 'Sigmar']
awesome_boolean = True


# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
exercise_2 = cool_string[:3]
print(exercise_2)


# Exercise 3: Use an index to grab the first element from your list.
exercise_3 = sick_list[0]
print(exercise_3)

# Exercise 4: Create a new number variable that adds 10 to your original number.
exercise_4 = nice_number + 10
print(exercise_4)

# Exercise 5: Use an index to get the last element in your list.
exercise_5 = sick_list[-1]
print(exercise_5)
 
# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
exercise_6 =names.split(',')
print(exercise_6)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
first_word = cool_string.split()[0]
first_word_upper =first_word.upper()
the_rest = cool_string[len(first_word):]
exercise_7 =first_word_upper + the_rest
print(exercise_7)
# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

print(f"In the year of {nice_number} nothing nice happened.")

# Exercise 9: Print “hello world”.
print('hello world')

