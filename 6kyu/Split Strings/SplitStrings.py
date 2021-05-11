# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd
# number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    output_list = []
    temp_str = ""
    counter = 0
    for x in s:
        if counter < 2:
            temp_str = temp_str + x
            counter += 1
        if counter == 2:
            counter = 0
            output_list.append(temp_str)
            temp_str = ""

    if temp_str != "":
        temp_str = temp_str + "_"
        output_list.append(temp_str)

    return output_list
