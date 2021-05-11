# Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed (like the name of this kata).
#
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
# Examples:
#
# spinWords("Hey fellow warriors") => "Hey wollef sroirraw"
# spinWords("This is a test") => "This is a test"
# spinWords("This is another test") => "This is rehtona test"

def spin_words(sentence):
    words = sentence.split()
    output = ""
    for x in words:
        if len(x) >= 5:
            x = x[::-1]
            output = output + x + " "
        else:
            output = output+x + " "
    output = output.rstrip()
    return output