# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
    text_string = ''
    numbers_string = ''
    numbers_string2 = ''
    zeros_string = ''
    if not strng:
        return '1'
    elif not strng[-1].isnumeric():
        return strng + '1'
    else:
        for x in reversed(strng):
            if not x.isnumeric():
                break
            numbers_string += x
        text_string = strng[:len(strng)-len(numbers_string)]
        numbers_string = numbers_string[::-1]
        numbers_string2 = str(int(numbers_string) + 1)
        if len(numbers_string) != len(numbers_string2):
            for x in range(len(numbers_string) - len(numbers_string2)):
                zeros_string += '0'
        return text_string + zeros_string + numbers_string2
