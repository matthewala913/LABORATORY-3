salary = float(input("Enter your monthly salary: "))

if salary >= 30000:
    print("You are eligible for the loan.")
     
    loan_amount = float(input("Enter the loan amount you are requesting: "))
    
    if loan_amount <= 10 * salary:
        months = int(input("Enter the number of months to pay off the loan: "))
        
        interest = 0.10 * loan_amount
        total_amount_with_interest = loan_amount + interest
        monthly_payment = total_amount_with_interest / months
        
        print(f"Total loan amount with interest: {total_amount_with_interest:.2f}")
        print(f"Monthly payment for the loan: {monthly_payment:.2f}")
    
    else:
        print("Loan amount requested is too high.")
else:
    print("You are not eligible for the loan.")