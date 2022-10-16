import connection
from functions import show_all, create_object, delete_object, setup_object, show_specific

# Connection
try:
    db = connection.connect()
    print('Connected to "%s" database' % db.name)
except:
    print('Connection failure')

rules = []

print('Greetings!')
while True:
    print('You have the following options to choose from:')
    print('1. View all premises')
    print('2. Add premises')
    print('3. Delete premises')
    print('4. Premises selection')
    print('5. View selected premises')
    print('6. Close application')
    a = input('Your choice: ')
    if a == '1':
        try:
            collection = db['buildings']
            show_all(collection)
        except:
            print('\nThe database does not contain premises')
    elif a == '2':
        try:
            collection = db['buildings']
            create_object(collection)
        except:
            print('\nError. Premise has not been added.')
    elif a == '3':
        try:
            collection = db['buildings']
            delete_object(collection)
        except:
            print('\nError. Premise has not been removed.')
    elif a == '4':
        try:
            collection = db['buildings']
            rules = setup_object(collection, rules)
        except:
            print('\nОшибка. Критерии не были установлены.')
    elif a == '5':
        try:
            collection = db['buildings']
            show_specific(collection, rules)
        except:
            print('\nError. Criteria have not been set.')
    else:
        quit()
