# This is a sample Python script.

'''You will construct a program that presents the quiz
to the user, checks the answer and gives some kind of feedback.
Your program will ask the user for their age, as this productivity
tool will only be suitable for ages 12-16. Your program will output
a suitable advice. '''

'''What inputs are required from the user? '''
def age_input(): #define an age functions to ask for input
    # the variable age will be an integer data type
    age = input("Please enter your age. You must be younger than 16 to use this tool. Your answer:")
    return age # this will return the value I have entered

def get_routine(): # this is another function that asks for input
    # the variable routine_focus will be a string data type
    routine_focus = input("What is your focus? Answer: ")
    return routine_focus

# the variable routines will be a list of options
routines = ["eat the frog", "visualise", "work out", "no email", "talk", "books"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print("Productivity tool ! Get Better You are Awesome")
    print(f"Your age is {age_input()}.")  # calls the function
    print(f"Your focus is {get_routine()}")
    print("your options are: ")
    for item in routines:
        print(item)

