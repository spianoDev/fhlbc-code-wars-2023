# Having two standards for a keypad layout is inconvenient!
# Computer keypad's layout:
# 7 8 9  \n
# 4 5 6  \n
# 1 2 3  \n
# 0 \n
#
# Cell phone keypad's layout:
# 1 2 3\n
# 4 5 6\n
# 7 8 9\n
# 0\n
#
# Solve the horror of unstandardized keypads by providing a function that converts computer
# input to a number as if it was typed on a phone.
#
# Example:
# "789" -> "123"
#
# Notes:
# You get a string with numbers only

def computer_to_phone(numbers):
    ascii_conversion = {
        48: 48,
        49: 55,
        50: 56,
        51: 57,
        52: 52,
        53: 53,
        54: 54,
        55: 49,
        56: 50,
        57: 51
    }

    print(numbers.translate(ascii_conversion))
    return numbers.translate(ascii_conversion)


computer_to_phone("0789456123") # => "0123456789"
computer_to_phone("000") # => "000"
computer_to_phone("94561") # => "34567"

