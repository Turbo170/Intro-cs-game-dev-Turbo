while True:
    try:
#user inputs number, float makes the number recognizable so words cant be used
        user_input = input("Enter a number: ")
        
        number = float(user_input)
        
        print(f"Valid number entered: {number}")
        break
        
    except ValueError:
        print("Error: That is not a number. Please try again.")
#except and ValueError to handle the error and require the user to use a number.