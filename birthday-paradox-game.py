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
    print("""
     Hello - want to learn a fun fact? walk into a room filled with people, and depending on the amount of people,
     there is a strong probability that mulitple people in that room share a birthday.
     I can demonstrate this to you with a series of trails.
     Lets begin!
      """)

def data ():
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day = list(range(1, 32)) # use list function to pass range(1,32), avoding to need to type 1 - 31
    sample_size = int(input('how many birthdays should I generate: ')) # moving to data() so its unaffeted by while loop
    return month, day, sample_size

'''
# lets try to use a random tool to select a month and day

random_month = random.choice(month)
random_day = random.choice(day)

print(f"The randomly selected date is {random_month} {random_day}")
print(type(random_month))

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

def calculate_random(month, day, sample_size): # lets calculate and display random_list, pass month, day rather than re-initilizing it inside the function
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

my function below has a few errors:
random_list = calculate_random() is generating a new random list, i do not want that, i want to keep the random list i generated in my function above

i need to fix my execption eroror message

based on some experiments, statistics.mode will always return a mode, if no repeating values
thus, to be in the safe side, its better to jsut use a dictionary 

def find_shared_bday(random_list):
    random_list = calculate_random()
    try:
        mode = statistics.mode(random_list)
        print(f"mutliple people share a birthday on: {mode[0]} {mode[1]}")
    except statistics.StatisticsError as e:
        if 'no unique mode' in str(e): # no unqiue mode signifies more than one mode
            print('multiple people share multiple birthdays')
        else:
            raise Exception("no birthdays found")

'''

def find_shared_bday(random_list): # passing random_list will keep the list generated in the above
    birth_month_day = {} # will store the key:value pairs
    for month, day in random_list: 
        birth_month_day[month, day] = birth_month_day.get((month, day), 0) + 1 # stores tuples in dictionary
    shared_birthday = False # created varible to avoid having return statements inside my for loop
    bday_key_set = set()
    for key, value in birth_month_day.items(): # key == (month, day) tuple, value == the count for each tuple, .items() is view-object of the key:value pair within the dictionary
        if value > 1:
            shared_birthday = True 
            bday_key_set.add(key)
            break # stops loop after first shared bday is found
    return shared_birthday, bday_key_set

def print_bday (shared_birthday, bday_key_set):
    if shared_birthday:
        for bday in bday_key_set:
            print(f"the birthday {bday[0]} {bday[1]} were shared by multiple people")
    else:
        print('no shared bday were found')
    

def initiate():
    instructions() 
    month, day, sample_size = data() # call data function to unpack its return values
    random_list = calculate_random(month, day, sample_size)
    shared_birthday, bday_key_set = find_shared_bday(random_list)
    print_bday(shared_birthday, bday_key_set)
    simulation_amount = 10
    print('now we will run the simulation ', simulation_amount, ' times')
    x = 0 # loop iterator
    bday_count = 0
    while x <= simulation_amount:
        random_list = calculate_random(month, day, sample_size)
        shared_birthday, bday_key_set = find_shared_bday(random_list) # even though i do not need bday_key_set, still refernce it in my while loop or else valuie error b/c two values will try to be placed into one
        if shared_birthday == True:
            bday_count += 1
        x += 1
    print(bday_count)



'''
keeping historical record of code that i am altering


def find_shared_bday(random_list): # passing random_list will keep the list generated in the above
    birth_month_day = {} # will store the key:value pairs
    for month, day in random_list: 
        birth_month_day[month, day] = birth_month_day.get((month, day), 0) + 1 # stores tuples in dictionary
    
    shared_birthday = False # created varible to avoid having return statements inside my for loop
    for key, value in birth_month_day.items(): # key == (month, day) tuple, value == the count for each tuple, .items() is view-object of the key:value pair within the dictionary
        if value > 1:
            print(f"the birthday {key[0]} {key[1]} were shared by multiple people")
            shared_birthday = True # removed the return from the for loop - it immeditly stops the loop after first iterator
            break
    if not shared_birthday:
        print('no birthdays were shared')
    # print(random_list) - needed for while loop to check if random_list changes or stays the same - confirmed it worked

    
def boolean_shared_bday(shared_birthday):
    shared_birthday = find_shared_bday()
    if shared_birthday == True:
        print('a birthday was shared by multiple people')
    print(shared_birthday)

def run_simulation(): # run simulation without printing each key, value pair from find_shared_bday()

def initiate():
    instructions() 
    month, day, sample_size = data() # call data function to unpack its return values
    sim_amount = 2
    x = 0
    while x <= sim_amount:
        random_list = calculate_random(month, day, sample_size)
        find_shared_bday(random_list)
        x += 1

def run_simulation():
    simulation_amount = 10
    print('now we will run the simulation ', simulation_amount, ' times')
    x = 0 # loop iterator
    while x <= simulation_amount:
        random_list = calculate_random(month, day, sample_size)
        shared_birthday = find_shared_bday(random_list)

'''

'''
Setting up the simulation
find_shared_bday() is the simulation - will need to be inside a while loop based on the total amount of desired simulation

wait - if i put a while loop over find_shared_bdaY() - it will continue looping using the same values from random_list - instead, i want the loop to restart with fresh new values
to see if a shared bday is found over n amount of simulations thus - i can ask the user once, then before i run the total x amount of simulations - i set the value of 
sample size = 25 hard coding the value and not needing to ask the for amount after each simulation

i can put the while loop on top of random_list = calculate_random() function, that way the random list gets generated after each iteration

update - the while loop prints out each time it runs, due to print statement in find_shared_bday()
thus, i should create another function soley for the simulation rounds

update pt2 - i believe an efficient route to take is to seperate the code that finds if shared from printing the amount

update pt3 - i have set up my simulation to handle multiple rounds without printing the random list each time

tracking simulation
i am not sure if i should create a function just to run the while loop (i should b/c i need to show the user the first round simulation)

update - i initially created a simulation function, but decided to just place the while loop inside the initiate function since everything has been called already

update - if i want to reference 


create a varible to determine the amount of times it runs
create a varible within find_shared_bday() to keep track of the amount of times it found a shared bday
after total amount of siumulations runs, peforme an average

'''

initiate()