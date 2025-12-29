#user inputs a name and age which both become variables for the if statement
print("What is your name?")
name = input()
age = int(input("How old are you?"))

"""if statment is used with age variable to print different sentences with name variable.
 elif is if else, used to give different sentences if something is other than, etc, etc"""
if (age) < 13:
    print(f"Hello {name}, you are a Child.")
elif age <= 18:
    print(f"Hello {name}), you are a Teenager.")
elif age < 25:
    print(f"Hello {name}, you are a Young Adult")
elif age >= 25:
    print(f"Hello {name}, you are an Adult.")