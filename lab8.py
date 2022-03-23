""" lab 8 """

#8.1

def count (str_input):
    
    return len(str_input.split())
    
#8.2

demo_str = 'hello world!' 

print(count(demo_str))

#8.3

def find_min_num(input_list):
    
    min_item = input_list[0]
    
    for num in input_list:
        if type(num) is not str:
            
            if min_item>= num:
                min_item = num
            
    return min_item    
    
#8.4

demo_list = [1,2,3,4,5,6]
print(find_min_num(demo_list))

#8.5
mix_list = [1,2,3,4,'a',5,6]
print(find_min_num(mix_list))


