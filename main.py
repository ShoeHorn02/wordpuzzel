
# Online Python - IDE, Editor, Compiler, Interpreter

#x is a string representing a book of text. The pages are separatd by \b. The lines by \n.

#Write a function that reverses the
#- order of pages
#- order of lines in each page
#- order of words in each line
#- don't reverse the characters in each word

#Sample string:
x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"


#Use: https://www.online-python.com

def removewhitespace(x):
    while("" in x) :
        x.remove("")
    return x

def addtosgring(x,a):
    d = []
    for i in x:
        i = str(i)+a
    return d.append(i)


def test(x):
    a = x.split('\b') #["the brown fox jumped over the fence\nthe brown bear fell down the hill\n","The big lion chased the deer\nThe monkey ate the bananas\n"]
    a = list(reversed(a)) #["The big lion chased the deer\nThe monkey ate the bananas\n", "the brown fox jumped over the fence\nthe brown bear fell down the hill\n"]
    y = removewhitespace(a)
    d = []
    for x in a:
        y = list(reversed(x.split('\n')))
        y = removewhitespace(y)
        for z in y:
            d.append(list(reversed(z.split(' '))))
    return ", ".join([" ".join(s) for s in d])

print(test(x))
