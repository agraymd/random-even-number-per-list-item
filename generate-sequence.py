'''
This program will generate a list of unique even numbers per person in the referenced list.
Could be made into a function, etc. but mainly stored here to document my own learning. 
The requirment was that each sequence number not be re-used for any person in the list.
To accomplish this I had to tackle two problems:

1. How to remember what numbers have been used alrady?
2. How to 'repeat an iteration' of the for loop if a previously used number is generated? 

#1 is achieved via initializing an empty list to store the values in as they are created successfully. 
#2 is achieved via a while loop checking that the generated number IS IN the list! 
If the number IS in the list, generate a new one until it is not (False condition breaks while loop -- key python concept here).
Once the number is unique (not in list yet), print the person and their number, then append the used number to the list storing used numbers.
At this point we move to the next item in the iterable (for loop) and a number is generated again. If the number is in the list already, 
the while loop will repeat and generate a new number until the condition is flase (number is unique) and continue with the else.
'''

import random

people_list = ['john', 'doe', 'jinglehimer', 'shmidt']

weekly_sequence = []

for person in people_list:
    sequence = random.randrange(2,101,2)
    while sequence in weekly_sequence:
        sequence = random.randrange(2,101,2)
    else:
        print(str(sequence) + ' ' + person)
        weekly_sequence.append(sequence)

