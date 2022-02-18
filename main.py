
# Online Python - IDE, Editor, Compiler, Interpreter

#x is a string representing a book of text. The pages are separatd by \b. The lines by \n.

#Write a function that reverses the
#- order of pages
#- order of lines in each page
#- order of words in each line
#- don't reverse the characters in each word

#Sample string:
input_book ="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"


#Use: https://www.online-python.com

def removewhitespace(x):
    while("" in x) :
        x.remove("")
    return x

def bookreverse(x):
    reversepage = list(reversed(x.split('\b') ))
    d = []
    for x in reversepage:
        reversesentence = list(reversed(x.split('\n')))
        reversesentence = removewhitespace(reversesentence)
        for z in reversesentence:
            d.append(list(reversed(z.split(' '))))
    return ", ".join([" ".join(s) for s in d])

print(bookreverse(input_book))
