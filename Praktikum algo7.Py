def add_suffix(number):
    last_digit = number % 10
    last_two_digits = number % 100

    if last_two_digits in [11, 12, 13]:
        suffix = 'th'
    elif last_digit == 1:
        suffix = 'st'
    elif last_digit == 2:
        suffix = 'nd'
    elif last_digit == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    return f"{number}{suffix}"
number = int(input("Masukkan angka: "))
print(f"Output: {add_suffix(number)}")
