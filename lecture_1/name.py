num = input('give me num: ')

try:
    if int(num) > 10:
        print(f'{num} mor than 10')

    else:
        print(f'{num} is less then 10')

except ValueError:
    print(f'"{num}" is not integer')

finally:
    print("done")

