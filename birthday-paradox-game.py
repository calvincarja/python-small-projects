import random
import statistics

'''
instructions:
i need to demonstrate to a user the birthday paradox.
SIMPLE APPROACH 
steps to demonstrate birthday paradox:
    provide a description of the birthday paradox to the user (complete)
    create a list of month and a list of day (complete)
    import random
    ask the user of sample size of birthdays to generate
    based on the sample size, a random selection from the month list, and a random selection of day will be selected 
    display the random select of month and day to the user - ensure the output is in readable format
    find the month + day combination repeated the most time, output this result to the user
'''

def instructions():
    return print("""
     Hello - want to learn a fun fact? walk into a room filled with people, and depending on the amount of people,
     there is a strong probability that mulitple people in that room share a birthday.
     I can demonstrate this to you with a series of trails.
     Lets begin!
      """)

def data ():
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day = list(range(1, 32)) # use list function to pass range(1,32), avoding to need to type 1 - 31
    return month, day
'''
# lets try to use a random tool to select a month and day

random_month = random.choice(month)
random_day = random.choice(day)

print(f"The randomly selected date is {random_month} {random_day}")
print(type(random_month))
'''

'''
# now lets try to display multiple random chocies of month and day
sample_size = 5
random_list = [(random.choice(month), random.choice(day)) for i in range(sample_size)] # [will contain the list] (is the tuples inside the list - seperated by a comma)
print(random_list)

# it worked, however the print output is not in the desired format
# str.format()
print('my list is: {}'.format(random_list))
# f-strings
print(f"my list is: {random_list[0]}")

# use a for loop to have more control over the output

for i in random_list:
    print(i)

# based on the for loop , i need to:
    # remove the quotation marks from the string
    # remove the comma between the month and day
    # remove the paranthesis from each value
    # since my list contains tuples, i can use two for loop iterator to address them each
'''
def calculate_random(): # lets calculate and display random_list
    month, day = data()
    sample_size = int(input('how many birthdays should I generate: '))
    random_list = [(random.choice(month), random.choice(day)) for i in range(sample_size)] # [will contain the list] (is the tuples inside the list - seperated by a comma)
    print(f"below are the {sample_size} birthdays:")
    results = ', '.join([f"{month} {day}" for month, day in random_list]) # in order to print in one line
    print(results)
    return random_list
'''
for month, day in random_list:
    print(f"{month} {day},")

the above for loop address all three concerns,
however I want the output to be in one line, 
to so, i need to store the output in a list, in order to use the .join() function
the problem ask to identify if a birthday is shared by more than 1 person, 
it does not ask me for the specific birthday(s), thus, finding the MODE is sufficient
'''

# sucess = print(mode) or print('The list contains multiple modes')
def calculate_mode(random_list):
    random_list = calculate_random()
    try:
        mode = statistics.mode(random_list)
        print(f"mutliple people share a birthday on: {mode[0]} {mode[1]}")
    except statistics.StatisticsError as e:
        if 'no unique mode' in str(e): # no unqiue mode signifies more than one mode
            print('multiple people share multiple birthdays')
        else:
            raise

'''
now i need my code to run x amount of times
each time it runs, it needs to keep track if a mode was found (single or multiple mode)
once the simulation is over, i need to output the amount of times a mode was found
i then divide by the x amount of times it ran, and generate a average percentage 
'''

