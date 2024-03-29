# The Menu
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola Bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai Iced": 3.99,
            "Irish Breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat White": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate Lava Cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice Pudding": 4.99,
        "Fried Banana": 4.49
    }
}

######################################################################################################################################################
########################################################################################################################################################

#Order sequence
#######################
### Note: The following dictonaries are defined to handle the options in the Menu dictionary
main_order = {}
order= {}
sub_order = {}

# count: Is used as a counter for the time the customer enters an invalid option
count=0
# incorrect : Is used to initiate and terminate the while loop that handles invalid entries
incorrect_choice = True

# This while loop keeps the order going until the customer continues to order or decides to finish it
while True:
    # start controls the squence if 'yes' proceeds if 'no' breaks
    start = input('Do wish to start your order? ').title()
    if start == 'Yes':
        count=0
        incorrect_choice = True
    
        print('Please choose from the following menus')
        for keys,values in menu.items():
            print(keys)
            
        #First level selection in the menu dictionary
        category = input("\nFrom which menu would you like to order?").title()
        
        #input control block
        count=0
        incorrect_choice = True
        if category not in menu.keys():
            while incorrect_choice:
                category = input('Your choice is not on the menu, please choose again: ').title()

                if category in menu.keys():
                    incorrect_choice = False
                elif count == 2:
                    print('Please start over\n\n')
                    incorrect_choice = False
                else:
                    count+=1
            
        #Menu print out       
        print(f'\nThese are our {category} options:')
        print("         Item name       | Price")
        print("-------------------------|-------")
        if type(values) is dict:
            for key,value in menu[category].items():
                if type(value) is float:
                    space = (25-len(key))*' ' 
                    print(f'{key}'+space+f'|{value}')
        
                elif type(value) is dict:
                    leading_space = 10*' '
                    trailing_space = (25-(10+len(key)))*' ' 
                    print("-------------------------|-------")
                    print(leading_space +f'{key}'+ trailing_space+'|')
    
                    for sub_key,sub_value in value.items():
                        sub_space = (25-len(sub_key))*' '
                        print(f'{sub_key}'+sub_space+f'|{sub_value}')
                    print("-------------------------|-------")

        #Second level input of the menu dictionary
        choice = input(f'\nPlease choose from the {category} menu: ').title()
        
        #input control block
        count=0
        incorrect_choice = True
        if choice not in menu[category].keys():
            while incorrect_choice:
                choice = input('Your choice is not on the menu, please choose again: ').title()
                if choice in menu[category].keys():
                    incorrect_choice = False
                elif count == 2:
                    print('Please start over\n\n')
                    incorrect_choice = False
                else:
                    count+=1
        #Quantity input
        if type(menu[category][choice]) is float:
            quantity = input(f'\n How many {choice} are you having today ? ')

            #input control
            count=0
            incorrect_choice = True
            if not quantity.isdigit():
                while incorrect_choice:
                    print('Please choose a whole number')
                    quantity = input(f'\n How many {choice} are you having today ? ')
                
                    if quantity.isdigit():
                        incorrect_choice = False
                    elif count == 2:
                        print('Please start over\n\n')
                        incorrect_choice = False
                    else:
                        count+=1
            #Order dictionary encompasses the first and second levels of the menu dictionary        
            order = {'choice':choice}
            order['price'] = menu[category][choice]
            order['quantity'] = int(quantity)

            if category in main_order.keys():
                main_order[category].append(order)
            else:
                main_order.update({category:[order]})
            
            
            
        elif type(menu[category][choice]) is dict:
            #Third level input in the menu dictionary
            sub_choice = input(f'Which kind of {choice} would you like? ').title()
            
            #input control block
            count=0
            incorrect_choice = True
            if sub_choice not in menu[category][choice].keys():
                while incorrect_choice:
                    sub_choice = input('Your choice is not on the menu, please choose again: ').title()
                
                    if sub_choice in menu[category][choice].keys():
                        incorrect_choice = False
                    elif count == 2:
                        print('Please start over\n\n')
                        incorrect_choice = False
                    else:
                        count+=1
        
        
        
            #Third level quatity input
            sub_quantity = input(f'\n How many {sub_choice} {choice}s are you having today ? ')

            #input control block
            count=0
            incorrect_choice = True
            if not sub_quantity.isdigit():
                while incorrect_choice:
                    print('Please choose a whole number')
                    sub_quantity = input(f'\n How many {choice} are you having today ? ')
                
                    if sub_quantity.isdigit():
                        incorrect_choice = False
                    elif count == 2:
                        print('Please start over\n\n')
                        incorrect_choice = False
                    else:
                        count+=1






            #The sub_order dictionary references the third level of the menu if necessary
            sub_order = {'choice':choice}
            sub_order['sub_choice'] = sub_choice
            sub_order['price'] = menu[category][choice][sub_choice]
            sub_order['sub_quantity'] = int(sub_quantity)

        
            if category in main_order.keys(): 
                main_order[category].append(sub_order)
            else:   
                main_order.update({category:[sub_order]})
            
        #Order continuation or termination block
        start = input('Do you wish to order something else? ').title()

        if start == 'Yes':
            pass
        elif start == 'No':
                break
        else:
            count = 0
            while count <=2:
                start = input('Please enter yes or no')
                count+=1
            break
                
        
        
    elif start == 'No':
        break
    else:
        start = input('Please enter yes or no: ')
        count+=1

# End of the ordering sequence
print('Thank you')
####################################################################################################################################################
###################################################################################################################################################

#The Bill

sub_total = 0

print("           Bill                    |          ")
print("-----------------------------------|----------")

#Order items parsing to calculate the bill
for keys,values in main_order.items():

    #Menu display
    leading_space = 10*' '
    trailing_space = (35-(10+len(keys)))*' '
    print(leading_space +f'{keys}'+ trailing_space+'|         ')
    for item in values:
        if len(item) == 3:
            choice_len = len(item['choice'])
            price_len = len(str(item['price']))
            quantity_len = len(str(item['quantity']))
            colon_len = len(': ')  
            item_total = item["price"]*item["quantity"]
            bill_space = (35-choice_len-price_len-colon_len-quantity_len-3)*' '
           
            print(f'{item["choice"]}'+': '+f'{item["price"]}*({item["quantity"]})'+bill_space+f'| {item_total} ')
        else:
            choice_len = len(item['choice'])
            sub_choice_len = len(item['sub_choice'])
            price_len = len(str(item['price']))
            quantity_len = len(str(item['sub_quantity']))
            colon_len = len(': ')  
            item_total = item["price"]*item["sub_quantity"]
            bill_space = (35-choice_len-price_len-colon_len-quantity_len-sub_choice_len-5)*' '

            print(f'{item["choice"]}'+f'({item["sub_choice"]})'+': '+f'{item["price"]}*({item["sub_quantity"]})'+bill_space+f'| {item_total} ')
        
        sub_total+=item_total
    
    
    
    
print("-----------------------------------|----------")
print(f'          Sub-total                | {sub_total:0.2f}')

gratuity = input(f'Suggested gratuity:\n18% --- {0.18*sub_total:0.2f}\n20% --- {0.20*sub_total:0.2f}\n22% --- {0.22*sub_total:0.2f}\nOther ***\n\nPlease select percentage: ')

#input control block
count=0
incorrect_choice = True
if not gratuity.isdigit():
    while incorrect_choice:
        gratuity = input(f'Please choose a whole number')
        
        if gratuity.isdigit():
            incorrect_choice = False
        elif count == 2:
            print('Please start over\n\n')
            incorrect_choice = False
        else:
            count+=1

#Final total calculation
tip = float(gratuity)/100 * sub_total
tax = sub_total*0.0875
total = sub_total+tip+tax

print("-----------------------------------|----------")
print(f'           Gratuity                | {tip:0.2f}')
print(f'           Sales Tax               | {tax:0.2f}')
print("-----------------------------------|----------")
print(f'           Total                   | {total:0.2f}')
print("\n\nThank You. See You Soon!!!")
