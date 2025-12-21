print("What is your name?")
name = input()
age = int(input("How old are you?"))

if (age) < 13:
    print(f"Hello {name}, you are a Child.")
elif age <= 18:
    print(f"Hello {name}), you are a Teenager.")
elif age < 25:
    print(f"Hello {name}, you are a Young Adult")
elif age >= 25:
    print(f"Hello {name}, you are an Adult.")