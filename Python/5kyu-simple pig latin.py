"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
"""

def pig_it(text):
    words = text.split(' ')
    pigworte = []
    for i in words:
        if i.isalpha():
            if len(i) > 1:
                pigworte.append(i[1:]+i[0]+'ay')
            else:
                pigworte.append(i + 'ay')
        else:
            pigworte.append(i)
    result = ' '.join(pigworte)
    return result