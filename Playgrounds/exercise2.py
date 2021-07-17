#Q1

# def temp_in_cel(temp_in_f):
#     temp_in_cel = (temp_in_f - 32) * (5/9)
#     return temp_in_cel

# print(temp_in_cel(10.10))

#Q2

# def is_odd(num):
#     if num % 2 == 0: #% = modulo
#         return False
#     else:
#         return True

# print(is_odd(-1))

#fizzbuzz

#Q3

# def mean(num_list):
#     return sum(num_list) / len(num_list)

# print(mean([4,3,2,6]))

# print(mean([10,5,6]))

#Q4

def total_cost(price,quantity):
    return price * quantity

print(f'${total_cost(4.25,3)}')

def total_cost(price,quantity):
    return f'${price * quantity}'

print(total_cost(4.25,3)+6)
