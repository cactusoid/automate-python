def func(x):
    intermediate_var = x**2 + x + 1

    if intermediate_var % 2:
        y = intermediate_var ** 3
    else:
        y = intermediate_var **3 + 1

    # setting attributes here
    func.optional_return = intermediate_var
    func.is_awesome = 'Yes, my function is awesome.'

    return y

y = func(3)
print('Final answer is', y)

# Accessing function attributes
print('Show calculations -->', func.optional_return)
print('Is my function awesome? -->', func.is_awesome)


my_list = ['some', 'list', 'containing', 'five', 'elements']

min_len = 3

for element in my_list:
    if len(element) < min_len:
        print(f'Caught an element shorter than {min_len} letters')
        break
else:
    print(f'All elements at least {min_len} letters long')