# Your task is to sort a given string. Each word in the string will contain a single number. This number is the
# position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid
# consecutive numbers.
#
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence):
    string = ""
    words = []
    sorted_sentence = ""
    if not sentence:
        return sentence
    else:
        for x in sentence:
            if x != " ":
                string = string + x
            else:
                words.append(string)
                string = ""
        words.append(string)
        print(words)
        for x in words:
            if "1" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "2" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "3" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "4" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "5" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "6" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "7" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "8" in x:
                sorted_sentence = sorted_sentence + x + " "
        for x in words:
            if "9" in x:
                sorted_sentence = sorted_sentence + x + " "
        sorted_sentence = sorted_sentence.rstrip()
        return sorted_sentence
