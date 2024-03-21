import random

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


print("""
     Hello - want to learn a fun fact? walk into a room filled with people, and depending on the amount of people,
     there is a strong probability that mulitple people in that room share a birthday.
     I can demonstrate this to you with a series of trails.
     Lets begin!
      """)
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day = list(range(1, 32)) # use list function to pass range(1,32), avoding to need to type 1 - 31

# lets try to use a random tool to select a month and day
random_month = random.choice(month)
random_day = random.choice(day)

print(f"The randomly selected date is {random_month} {random_day}")

# now lets try to display multiple random chocies of month and day
sample_size = 5
random_list = [(random.choice(month), random.choice(day)) for i in range(sample_size)]
print(random_list)

# it worked, however the print output is not in the desired format