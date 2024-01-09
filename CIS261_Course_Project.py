import datetime

def validate_date_format(date):
    try:
        datetime.datetime.strptime(date, '%m%d%Y')
        return True
    except ValueError:
        return False

def custom_round(number: float):
    return "{:.2f}".format(number)

def collect_employee_name():
    return input("Employee Name: ")

def collect_date_range():
    from_date = None
    to_date = None
    
    while from_date == None:
        date = input('What is the first day of work? (MM/DD/YYYY): ')
        is_date_valid = validate_date_format(date)
        
        if is_date_valid:
            from_date = date
        else:
            print('Date format is incorrect. Please Try again.')
            
    while to_date == None:
        date = input('What is the last day of work? (MM/DD/YYYY): ')
        is_date_valid = validate_date_format(date)
        
        if is_date_valid:
            to_date = date
        else:
            print('Date format is incorrect. Please Try again.')
    
    return from_date, to_date

def collect_hours_worked():
    hours_worked = None
    while hours_worked == None:
        try:
            hours_worked = float(input("Hours Worked: "))
        except ValueError:
            print('The decimal was incorrect. Please Try Again.')
    return hours_worked

def collect_hourly_rate():
    hourly_rate = None
    while hourly_rate == None:
        try:
            hourly_rate = float(input("Hourly Rate: "))
        except ValueError:
            print('The decimal was incorrect. Please Try Again')
    return hourly_rate

def collect_tax_rate():
    tax_rate = None
    while tax_rate == None:
        try:
            tax_rate = float(input("Income Tax Rate (%): "))
        except ValueError:
            print('The decimal was incorrect. Please Try Again.')
    return tax_rate

def calculate_income_data(hours_worked, hourly_rate, tax_rate):
    gross_pay = hourly_rate * hours_worked
    income_tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - income_tax
    
    return gross_pay, income_tax, net_pay

def main():
    while True:
        employee_information = open('employee_information.txt', 'a+')
        
        employee_name = collect_employee_name()
         if employee_name == "End":
            employee_information.seek(0)
            display_data(employee_information) # left off here

        from_date, to_date = collect_date_range()
        hours_worked = collect_hours_worked()
        hourly_rate = collect_hourly_rate()
        tax_rate = collect_tax_rate()
        
        gross_pay, income_tax, net_pay = calculate_income_data(hours_worked, hourly_rate, tax_rate)
        
        data = [employee_name, hourly_rate, from_date, to_date, hours_worked, income_tax, tax_rate, gross_pay, net_pay]
        
        employee_information.write('|'.join(map(str, data)) + '\n')
        employee_information.close()

main()