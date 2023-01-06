annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
portion_down_payment = (total_cost * .25)
monthly_salary = annual_salary/12 
monthly_savings = monthly_salary * portion_saved
month_counter = 0
current_savings = 0
while current_savings < portion_down_payment:
    month_counter += 1 
    current_savings += (current_savings * (.04/12)) + monthly_savings
    if (month_counter % 6 == 0):
        annual_salary += (annual_salary * semi_annual_raise) 
        monthly_salary = annual_salary/12 
        monthly_savings = monthly_salary * portion_saved
print('Number of months : ', month_counter)  

