def main():

    years = 5
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value is", principal)

main()