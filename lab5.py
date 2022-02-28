''' 
lab 5
'''

#5.1

alien_colour = 'green'
if alien_colour == 'green':
    print('You just earned 5 points.')

#5.2

alien_colour = 'red'

if alien_colour == 'green':
    print('You just earned 5 points.')
    
else:
    print('You just earned 10 points.')

#5.3

favourite_fruits = ['pears', 'apples', 'kiwis']

if 'pears' in favourite_fruits:
    print('You really like pears!')

if 'apples' in favourite_fruits:
    print('You really like apples!')
    
if 'kiwis' in favourite_fruits:
    print ('You really like kiwis!')
    
#5.4

age = 20

if age < 10 :
    print('You are a kid.')
    if age > 65:
        print('You are an elder.')
elif age < 20:
    print('You are a teenager.')
else:
    print('You are an adult.')
    


    