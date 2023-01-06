## Going to start with the input portions which is easy enough, then all the formulas will be kind of hard to work through

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = (total_cost * .25)
monthly_salary = annual_salary/12 
monthly_savings = monthly_salary * portion_saved
month_counter = 0
current_savings = 0
while current_savings < portion_down_payment:
    month_counter += 1 
    current_savings += (current_savings * (.04/12)) + monthly_savings
print('Number of months : ', month_counter) 

## Problems arised when += wasnt used in Line 13, figured out using a regular "=" expression will lead to problems

