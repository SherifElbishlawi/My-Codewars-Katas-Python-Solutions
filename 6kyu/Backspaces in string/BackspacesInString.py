# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#
# Your task is to process a string with "#" symbols.
#
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    output_string = ''
    for x in s:
        if x != '#':
            output_string += x
        else:
            output_string = output_string[:-1]
    return output_string

