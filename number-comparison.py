first_number= input()
second_number= input()
first_digits= tuple(map(int, first_number[::-1]))
second_digits= tuple(map(int, second_number[::-1]))
if first_digits < second_digits:
    print(first_number,"<", second_number)
elif first_digits > second_digits:
    print(second_number,"<", first_number)
else:
    print(first_number,"=", second_number)

    
