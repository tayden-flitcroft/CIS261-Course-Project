def custom_round(number: float):
    return "{:.2f}".format(number)

def collect_employee_name():
    return input("Employee Name: ")

def collect_date_range():
    from_date = input('What is the first day of work? (MM/DD/YYYY): ')
    to_date = input('What is the last day of work? (MM/DD/YYYY): ')
    
    return from_date, to_date
    

def collect_hours_worked():
    return float(input("Hours Worked: "))

def collect_hourly_rate():
    return float(input("Hourly Rate: "))

def collect_tax_rate():
    return float(input("Income Tax Rate (%): "))

def calculate_income_data(hours_worked, hourly_rate, tax_rate):
    gross_pay = hourly_rate * hours_worked
    income_tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - income_tax
    
    return gross_pay, income_tax, net_pay

def display_employee_data(employee):
    print(f"""
    Name: {employee["name"]}
    From Date: {employee["from_date"]}
    To Date: {employee["to_date"]}
    Total Hours Worked: {employee["hours_worked"]}
    Hourly Rate: ${custom_round(employee["hourly_rate"])}
    Gross Pay: ${custom_round(employee["gross_pay"])}
    Income Tax: ${custom_round(employee["income_tax"])}
    Net Pay: ${custom_round(employee["net_pay"])}
""")
    
def display_total_employee_data(data):
    print(f"""
    Total Employees: {data["total_employees"]}
    Total Hours Worked: {data["hours_worked"]}
    Total Gross Pay: ${custom_round(data["gross_pay"])}
    Total Tax: ${custom_round(data["income_tax"])}
    Total Net Pay: ${custom_round(data["net_pay"])}
""")      
    
def display_totals(all_employee_data, total_employee_data):
    display_total_employee_data(total_employee_data)
    
    for employee in all_employee_data:
        display_employee_data(employee)
        
def main():
    total_employee_data = {
        "total_employees": 0,
        "hours_worked": 0,
        "gross_pay": 0,
        "income_tax": 0,
        "net_pay": 0
    }
    
    all_employees_data = []
    
    while True:
        temp_employee_data = {}

        from_date, to_date = collect_date_range()
        employee_name = collect_employee_name()
        
        if employee_name == "End":
            break
        
        hours_worked = collect_hours_worked()
        hourly_rate = collect_hourly_rate()
        tax_rate = collect_tax_rate()
        
        gross_pay, income_tax, net_pay = calculate_income_data(hours_worked, hourly_rate, tax_rate)

        total_employee_data = {
            "total_employees": total_employee_data["total_employees"] + 1,
            "hours_worked": total_employee_data["hours_worked"] + hours_worked,
            "gross_pay": total_employee_data["gross_pay"] + gross_pay,
            "income_tax": total_employee_data["income_tax"] + income_tax,
            "net_pay": total_employee_data["net_pay"] + net_pay
        }
        
        all_employees_data.append({
            "from_date": from_date, 
            "to_date": to_date, 
            "name": employee_name,
            "hourly_rate": hourly_rate,
            "hours_worked": hours_worked,
            "income_tax": income_tax,
            "income_tax_rate": tax_rate,
            "gross_pay": gross_pay,
            "net_pay": net_pay
            
            
        })

    display_totals(all_employees_data, total_employee_data)
        
main()