## Til's Cost of Vacancy Calculator Script

# editable variables list
annual_revenue= 10000000
number_of_employees=100
working_days_per_year=260
revenue_impact_multiplier=3 # 1,2 or 3 depending on level and prioity of role
estimated_time2fill=180
example_employee_salary=170000
 
## DETERMINE REVENUE LOST 
 
# STEP 1: CALCULATE AVERAGE EMPLOYEE REVENUE
average_employee_revenue = annual_revenue // number_of_employees #round to whole $
print("Determine the average employee revenue by dividing the company’s annual revenue by the total number of employees in the organization." 
" Then, multiply that number by 260*, the average number of working days per year, to determine the daily employee revenue.\nAnnual revenue:",annual_revenue,", Number of employees:",number_of_employees,"Average employee revenue: $",average_employee_revenue)

average_daily_employee_revenue = average_employee_revenue // working_days_per_year
print("Daily employee revenue:",average_daily_employee_revenue)

# STEP 2: CALCULATE ROLE-SPECIFIC REVENUE
daily_role_specific_revenue = average_daily_employee_revenue * revenue_impact_multiplier
print("Then, estimate a specific role’s revenue by utilizing a predetermined multiplier, which helps quantify revenue based on the role’s level of impact in the company." 
"Multiply the daily salary by one for a vacant entry-level role such as a coordinator or junior-level contributor. Use two for high-impact roles like sales persons, tech employees and product developers. Multiply the daily salary by three for executive and leadership roles. \n"
,daily_role_specific_revenue)

# STEP 3: CALCULATE REVENUE LOST TO VACANT ROLE 
revenue_lost2vacant_role = daily_role_specific_revenue * estimated_time2fill
print(f'Revenue lost to vacant role: ${revenue_lost2vacant_role}')

## DETERMINE PAYROLL AND BENEFITS SAVINGS

# STEP 1 = CALCULATE COST OF EMPLOYEE
cost_of_benefits = example_employee_salary * (.314)
cost_of_employee = example_employee_salary + cost_of_benefits 
print(f'Cost of benefits: ${cost_of_benefits}, Cost of employee: ${cost_of_employee}')

# STEP 2: CALCULATE PAYROLL AND BENEFITS SAVINGS
daily_cost_of_employee = cost_of_employee // 260
payroll_and_benefits_savings = daily_cost_of_employee * estimated_time2fill
print(f'Daily cost of employee: ${daily_cost_of_employee}, Payroll and benefits savings: ${payroll_and_benefits_savings}')

## CALCULATE THE COST-OF-VACANCY

cost_of_vacancy = revenue_lost2vacant_role - payroll_and_benefits_savings
print(f'Cost of vacancy: ${cost_of_vacancy}')