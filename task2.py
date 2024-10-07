import random
def get_number_tickets(min,max,quantity):
    if min < 1 or min > max:
        return 'Your min is out of range'
    elif max > 1000:
        return 'Your max is out of range'
    elif not(quantity<max and quantity>min and quantity <= ((max - min + 1))):
        return 'Your quantity id out of range'
    else:
        res_list = []
        i = 0
        while i < quantity:
            temprand = random.randint(min,max)
            if(not (temprand in res_list)):
                res_list.append(temprand)
                i+=1
        res_list.sort()
        return res_list
min = int(input('Enter min: '))
max = int(input ('Enter max: '))
quantity = int(input('Enter quantity: '))
print(get_number_tickets(min,max,quantity))
