import csv

def get_all_user_data():
    doc = open('authorization.txt')
    data = list(csv.DictReader(doc, delimiter="|"))
    doc.close()
    return data

def get_all_user_ids():
    return [i['id'] for i in get_all_user_data()]

def add_user_data(id, password, authorization):
    doc = open('authorization.txt', 'a+')
    doc.write('|'.join([id, password, authorization]) + '\n')
    doc.close()

def display_user_data(data):
    print()
    print('User Id:', data['id'])
    print('Password:', data['password'])
    print('Authorization:', data['authorization'])

def main():
    ids = get_all_user_ids()

    while True:
        while True:
            user_id = input('User ID (or End): ')
            if user_id not in ids:
                break
            print('User ID already present. Please enter a unique User ID.')

        if user_id == 'End':
            for user in get_all_user_data():
                display_user_data(user)

            print('Good Bye!')
            break

        password = input('Password: ')

        while True:
            authorization = input('Authorization Code (Admin/User): ')
            if authorization == 'Admin' or authorization == 'User':
                break
            print('Please enter either Admin or User for Authorization Code.')

        add_user_data(user_id, password, authorization)

if __name__ == '__main__':
    main()