import datetime
from csv import DictReader

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def get_all_user_data():
    doc = open('authorization.txt')
    data = list(DictReader(doc, delimiter="|"))
    return data

def login():
    all_users = get_all_user_data()

    user_id = input('User ID: ')
    password = input('Password: ')
    
    user_dict = list(filter(lambda x: x['id'] == user_id, all_users))

    if not bool(user_dict):
        print('User ID does not exist.')
        exit()

    if user_dict[0]['password'] != password:
        print('Password is incorrect.')
        exit()

    return Login(user_id, password, user_dict[0]['authorization'])

def validate_date_format(date):
    try:
        datetime.datetime.strptime(date, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def custom_round(number: float):
    return "{:.2f}".format(number)

def collect_employee_name():
    return input('Employee Name (or "End"): ')

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

def display_data(current_user):
    totals = {
        "hours_worked": 0,
        "income_tax": 0,
        "net_pay": 0,
        "number_of_employees": 0
    }

    while True:
        date_to_display = input('What starting date should be used to run the report? (MM/DD/YYYY or "All"): ')
        if date_to_display == 'All' or validate_date_format(date_to_display):
            break
        print('Date format is incorrect. Please Try again.')

    employee_information_file = open('employee_information.txt')
    employee_information = list(DictReader(employee_information_file, delimiter='|'))
    employee_information_file.close()

    if date_to_display != 'All':
        employee_information = list(filter(lambda x: x['from_date'] == date_to_display, employee_information))

    print('User ID:', current_user.user_id)
    print('Password:', current_user.password)
    print('Authorization Code:', current_user.authorization)    
    print()

    for employee in employee_information:
           totals["number_of_employees"] += 1
           totals["hours_worked"] += float(employee["hours_worked"])
           totals["income_tax"] += float(employee["income_tax"])
           totals["net_pay"] += float(employee["net_pay"])

           print(f'''
{employee["name"]}:
    From Date: {employee["from_date"]}
    To Date: {employee["to_date"]}
    Hours Worked: {employee['hours_worked']}
    Hourly Rate: {employee["hourly_rate"]}
    Gross Pay: {employee["gross_pay"]}
    Income Tax Rate: {employee["tax_rate"]}
    Income Tax: {employee["income_tax"]}
    Net Pay: {employee["net_pay"]}
''')
           
    print(f'''
Totals:
    Number of Employees: {totals["number_of_employees"]}
    Hours Worked: {totals["hours_worked"]}
    Income Tax: {totals["income_tax"]}
    Net Pay: {totals["net_pay"]}
''')
    
    print('Bye!')
    exit()


def main():
    current_user = login()

    if current_user.authorization == 'User':
        display_data(current_user)

    while True:
        employee_name = collect_employee_name()
        if employee_name == "End":
            display_data(current_user)

        from_date, to_date = collect_date_range()
        hours_worked = collect_hours_worked()
        hourly_rate = collect_hourly_rate()
        tax_rate = collect_tax_rate()
        
        gross_pay, income_tax, net_pay = calculate_income_data(hours_worked, hourly_rate, tax_rate)
        
        data = [employee_name, hourly_rate, from_date, to_date, hours_worked, income_tax, tax_rate, gross_pay, net_pay]

        employee_information = open('employee_information.txt', 'a+')
        employee_information.write('|'.join(map(str, data)) + '\n')
        employee_information.close()

if __name__ == '__main__':
    main()