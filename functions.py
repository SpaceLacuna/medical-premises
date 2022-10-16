import pymongo
from prettytable import PrettyTable


def create_collection(db, name):
    collection = db[name]
    return collection


def create_object(collection):
    print("Adding a new room.\n")
    new_object = {}
    new_object['title'] = input('title: ')
    new_object['width'] = int(input('width: '))
    new_object['length'] = int(input('length: '))
    new_object['area'] = int(input('area: '))
    new_object['floors'] = int(input('floors: '))
    new_object['toilet_rooms'] = int(input('toilet_rooms: '))
    new_object['emergency_exits'] = int(input('emergency_exits: '))
    print(new_object)
    ins_result = collection.insert_one(new_object)


def setup_object(collection, rules):
    if not rules:
        rules = [
                    {'area': {'$gte': 0}},
                    {'toilet_rooms': {'$gte': 0}},
                    {'emergency_exits': {'$gte': 0}},
                    {'floors': {'$lte': 10000}},
                ]
    while True:
        print('\nYou have the following options to choose from:')
        print('1. Set minimum area')
        print('2. Set a minimum number of toilets')
        print('3. Set the minimum number of emergency exits')
        print('4. Set the maximum number of floors')
        print('5. Finish setting')
        a = input('Your choice: ')
        if a == '1':
            min_area = int(input('Enter value(minimum area): '))
            rule_area = {'area': {'$gte': min_area}}
        elif a == '2':
            min_toilets = int(input('Enter value(minimum number of toilets): '))
            rule_toilets = {'toilet_rooms': {'$gte': min_toilets}}
        elif a == '3':
            min_exits = int(input('Enter value(minimum number of emergency exits): '))
            rule_exits = {'emergency_exits': {'$gte': min_exits}}
        elif a == '4':
            max_floors = int(input('Enter value(maximum number of floors): '))
            rule_floors = {'floors': {'$lte': max_floors}}
        elif a == '5':
            break
    # Rule update
    for i in range(0, len(rules)):
        if 'area' in rules[i].keys() and 'rule_area' in locals(): rules[i] = rule_area
        if 'toilet_rooms' in rules[i].keys() and 'rule_toilets' in locals(): rules[i] = rule_toilets
        if 'emergency_exits' in rules[i].keys() and 'rule_exits' in locals(): rules[i] = rule_exits
        if 'floors' in rules[i].keys() and 'rule_floors' in locals(): rules[i] = rule_floors
    return rules


def delete_object(collection):

    title = input('\nEnter the title of premise: ')
    my_query = {'title': title}
    collection.delete_many(my_query)


def show_specific(collection, rules):
    mytable = PrettyTable()
    mytable.field_names = ['title', 'area', 'floors', 'toilet_rooms', 'emergency_exits']
    for channel in collection.find({'$and': rules}):
        mytable.add_row([channel['title'], channel['area'], channel['floors'], channel['toilet_rooms'], channel['emergency_exits']])
        print('\nPremises that meet the given conditions:')
        print(mytable)


def show_all(collection):
    mytable = PrettyTable()
    mytable.field_names = ['title', 'area', 'floors', 'toilet_rooms', 'emergency_exits']
    for channel in collection.find():
        mytable.add_row([channel['title'], channel['area'], channel['floors'], channel['toilet_rooms'], channel['emergency_exits']])
    print('\nAll available premises:')
    print(mytable)
    