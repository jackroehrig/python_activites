def hello():
    print('Hello there...')

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(list):
    if(len(list) == 0):
        print('My lunchbox is empty!')
    else:
        for item in list:
            if(list.index(item) == 0):
                print(f'First I eat {item}')
            else:
                print(f'Then I eat {item}')

hello()
print(pack('shirt', 'shoes', 'shorts'))
eat_lunch(['Mac & Cheese', 'Hot Dogs'])