# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    r_string = ''
    g_string = ''
    b_string = ''
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    r = hex(r)
    r = r[2:]
    r_string = str(r).upper()
    g = hex(g)
    g = g[2:]
    g_string = str(g).upper()
    b = hex(b)
    b = b[2:]
    b_string = str(b).upper()
    if len(r_string) == 1:
        r_string = '0' + r_string

    if len(g_string) == 1:
        g_string = '0' + g_string

    if len(b_string) == 1:
        b_string = '0' + b_string

    return r_string + g_string + b_string


print(rgb(255, 0, 1))
