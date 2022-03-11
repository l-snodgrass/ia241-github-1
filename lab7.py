"""
lab7
"""

#7.1

i = 0
while i <= 5:
    if i != 3:
        print(i)
   
    i += 1
    
#7.2

i = 5
result = 1

while 0 < i <= 5:
    result *= i
    i -= 1
    
print(result)

#7.3
i = 1
result = 0

while 1 <= i <= 5:
    result += i
    i += 1
    
print(result)
    
#7.4

i = 3
result = 1

while 3 <= i <= 8:
    result *= i
    i += 1

print(result)

#7.5

i = 4
result = 1 

while i <= 8:
    result *= i
    i += 1

print(result)

#7.6

num_list = [12, 32, 43, 35]

while num_list:
    num_list.remove(num_list[0])
    
print(num_list)
    