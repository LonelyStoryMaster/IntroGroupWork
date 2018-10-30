#Problem 1: Initials
def name():
    fullName = input('Enter your first, middle, and last name:\n')
    return fullName

def split_name(name):
    part = name.split()
    return part

def initials(nList):
    initials = ''
    for i in range(len(nList)):
        initials += nList[i][0] + '.'
    print(initials)

#Problem 5: Alphabetic Telephone Number Translator
def telephone():
    letter_nums = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
                   ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
    return_num = []
    phone = input("Enter a phone number (XXX-XXX-XXXX):\n")
    phone = phone.upper()
    for x in phone:
        if x in letter_nums[0]:
            return_num.append('2')
        elif x in letter_nums[1]:
            return_num.append('3')
        elif x in letter_nums[2]:
            return_num.append('4')
        elif x in letter_nums[3]:
            return_num.append('5')
        elif x in letter_nums[4]:
            return_num.append('6')
        elif x in letter_nums[5]:
            return_num.append('7')
        elif x in letter_nums[6]:
            return_num.append('8')
        elif x in letter_nums[7]:
            return_num.append('9')
        else:
            return_num.append(x)
    return_phone = ''.join(return_num)
    print(return_phone)
    return return_phone

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
    return vowel

def count_consonants(string):
    consonants = ['q', 'w', 'r', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    count = 0
    for ch in string.lower():
        if ch in consonants:
            count += 1
    print("Number of consonants found:", count)
    return count

def count_things():
    vowels = ['e', 'y', 'u', 'i', 'o', 'a']
    user_input = input("Please enter a string:\n")
    user_input = user_input.lower()
    count_consonants(user_input)
    vowel(user_input, vowels)

#Problem 12: Pig Latin
def pig_latin():
    pig_sentance = ''
    sentance = input("Enter a sentance to be translated:\n")
    sentance = sentance.upper()
    words = sentance.split()
    for word in words:
        new_word = word[1:]
        letter = word[:1]
        new_word += letter + 'AY'
        pig_sentance += new_word + ' '
    print(pig_sentance)
    return pig_sentance

#Running everything
if __name__ == '__main__':
    initials(split_name(name()))
    print()
    telephone()
    print()
    count_things()
    print()
    pig_latin()