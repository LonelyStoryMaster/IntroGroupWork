#Problem 1: Initials
def name():
    fullName = input('Enter your first, middle, and last name:\n')
    return fullName

def split(name):
    part = name.split()
    return part

def initials(nList):
    first = nList[0]
    mid = nList[1]
    last = nList[2]
    initF = first[0:1]
    initM = mid[0:1]
    initL = last[0:1]
    print('User\'s initials %s. %s. %s.' % (initF, initM, initL))


#Problem 5: Alphabetic Telephone Number Translator
def translator(num1,num2,num3,num4,num5,num6,num7,num8):
    newNum = []
    phone = input('Enter a phone number(nnn-nnn-nnnn):')
    for x in phone:
        if x in num1:
            newNum.append('2')
        elif x in num2:
            newNum.append('3')
        elif x in num3:
            newNum.append('4')
        elif x in num4:
            newNum.append('5')
        elif x in num5:
            newNum.append('6')
        elif x in num6:
            newNum.append('7')
        elif x in num7:
            newNum.append('8')
        elif x in num8:
            newNum.append('9')
        else:
            newNum.append(x)
    newNum = ''.join(newNum)
    print(newNum)


#Problem 9: Vowels and Consonants
def vowel(string, vow):
    vowel = 0
    string = string.lower()
    for x in string:
        if x in vow:
            vowel += 1
        else:
            continue
    print('Number of vowels is %d' % vowel)

def consonant(string, cons):
    consonant = 0
    string = string.lower()
    for x in string:
        if x in cons:
            consonant += 1
        else:
            continue
    print('Number of consonants is %d' % consonant)


#Problem 12: Pig Latin
def pigLatin():
    z = 0
    newPhrase = []
    phrase = input('Enter a sentence: ')
    words = phrase.split()
    newPhrase = words
    for x in words:
        new_Word = x + x[0] + 'ay'
        newPhrase[z] = new_Word[1:len(phrase)]
        z += 1
    print(' '.join(newPhrase))

    
if __name__ == '__main__':
    #Problem 1: Initials
    nameList = []
    userName = name()
    nameList = split(userName)
    print('User\'s first, middle and last name:', nameList)
    initials(nameList)
    print()

    
    #Problem 5: Alphabetic Telephone Number Translator
    num1 = ['A','B','C']
    num2 = ['D','E','F']
    num3 = ['G','H','I']
    num4 = ['J','K','L']
    num5 = ['M','N','O']
    num6 = ['P','Q','R','S']
    num7 = ['T','U','V']
    num8 = ['W','X','Y','Z']
    translator(num1,num2,num3,num4,num5,num6,num7,num8)


    #Problem 9: Vowels and Consonants
    vowels = ['a', 'e', 'i', 'u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    usrString = input('Enter a word or phrase:')
    vowel(usrString, vowels)
    consonant(usrString, consonants)

    #Problem
    pigLatin()
