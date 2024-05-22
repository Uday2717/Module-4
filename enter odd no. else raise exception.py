def get_odd_number():
    while True:
        try:
            number = int(input("Enter an odd number: "))
            if number % 2 != 0:
                return number
            else:
                raise ValueError("Even number entered. Please enter an odd number.")
        except ValueError as e:
            print(e)


try:
    odd_number = get_odd_number()
    print("You entered:", odd_number)
except ValueError as e:
    print(e)
