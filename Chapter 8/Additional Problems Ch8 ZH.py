###Problem 1: Rain fall count
##def rainCount():
##    rain = []
##    for x in range(12):
##        rain.append(float(input('Enter the amount of range for %s (in inches):' % (months[x]))))
##    return rain
##
##def rainCalc(months, rainList):
##    #Total Amount of Range
##    print('The total amount of rain during the year is: %0.2f' % sum(rainList))
##    #Average of total rainfall
##    avg = sum(rainList)/ len(rainList)
##    print('Average rain fall for the year is: %0.2f inche(s)' % avg)
##    #Finding min and max rainfall
##    highTotal = max(rainList)
##    maxLoc = rainList.index(highTotal)
##    minTotal = min(rainList)
##    minLoc = rainList.index(minTotal)
##    #Printing min and max rainfall
##    print('The month with the highest rain total had', highTotal, 'inches in', months[maxLoc])
##    print('The month with the lowest rain total had', minTotal, 'inches in', months[minLoc])
##    print()
##    print()




#Problem 2: Create own list functions
##def menu():
##    print('a - To add items to your shopping list')
##    print('d - To delete items to your shopping list')
##    print('f - To search for an item')
##    print('s - To sort list alphabetically')
##    print('q - to quit this program')
##
##   
##def addList():
##    theList = []
##    item =input('Enter a item for your shopping list:\n')
##    while item != 'q':
##        theList.append(item)
##        item =input('Enter another item for your shopping or q to quit:\n')
##    print('Current list is:', theList)
##    return theList
##
##
##def delList(remList):
##    removes = input('Enter the name of the item you want to remove\n')
##    while removes != 'q':
##        remList.remove(removes)
##        removes = input('Enter the name of the item you want to remove or q to quit\n')
##    print('Current list is:', remList)
##    return remList
##
##
##def searchList(lookList):
##    y = 0
##    z = 0
##    search = input('Enter the name of the item you want to check for\n')
##    while search != 'q':
##        for x in lookList:
##            if x == search:
##                y += 1
##                z += 1
##                print(search, 'is item', z, 'on the list')
##            else:
##                print('Searching...')
##                z += 1
##        print('The item is on your list', y, 'times')
##        search = input('Enter the name of another item you want to check for or q for quit\n')
##        y = 0
##        z = 0
##
##
##def sortList(alphaList):
##    alphaList.sort()
##    print(alphaList)
   


#Problem 3: Encrypting and Decrypting
def encrypt(codes):
    newSecret = []
    secret = input('Enter a word or phrase to encrypt:\n')
    for x in secret:
        if x in codes:
            newSecret.append(codes[x])
    newSecret = ''.join(newSecret)
    print(newSecret)
    return(newSecret)

def decrypt(codes):
    newPhrase = []
    letters = []
    symbols = []
    phrase = input('Enter a word or phrase to decrypt:\n')
    for letter, symbol in codes.items():
        letters.append(letter)
        symbols.append(symbol)
    for x in phrase:
        if x in symbols:
            newPhrase.append(letters[symbols.index(x)])
    newPhrase = ''.join(newPhrase)
    print(newPhrase)
        
            

if __name__ == '__main__':
##    #Problem 1
##    months= ['January', 'February', 'March', 'April', 'May', 'June',
##             'July', 'August', 'September', 'October', 'November', 'December']
##    rain = rainCount()
##    rainCalc(months, rain)



    #Problem 2
##    newList = []
##    myList = []
##    menu()
##    x = input('Enter a letter based on what option you need:\n')
##    while x != 'q':
##        if x == 'a':
##            myList = addList()
##            x = input('Continue to menu another option or q to quit\n')
##        elif x == 'd':
##            myList = delList(myList)
##            x = input('Continue to menu another option or q to quit\n')
##        elif x == 'f':
##            searchList(myList)
##            x = input('Continue to menu another option or q to quit\n')
##        elif x == 's':
##            myList = sortList(myList)
##            x = input('Continue to menu another option or q to quit\n')
##        else:
##            print('ERROR: You entered a letter not in the menu!')
##            x = input('Continue to menu another option or q to quit\n')

    #Problem 3
    codes = {'A': '1', 'a': '♫', 'B': '2', 'b': '@', 'C': '3', 'c': '#', 'D': '4', 'd': '$', 'E': '5', 'e': '%',
             'F': '6', 'f': '^', 'G': '7', 'g': '&', 'H': '8', 'h': '*', 'I': '9', 'i': '▓', 'J': '9', 'j': ')',
             'K': '[', 'k': '{', 'L': ']', 'l': '}', 'M': '≥', 'm': '|', 'N': ';', 'n': ':', 'O': "'", 'o': '♪',
             'P': ',', 'p': '<', 'Q': '.', 'q': '>', 'R': '/', 'r': '?', 'S': '`', 's': '~', 'T': '☺', 't': '▬',
             'U': '♦', 'u': '♣', 'V': '♠', 'v': '♂', 'W': '╝', 'w': '☼', 'X': '!', 'x': '(', 'Y': '±', 'y': '►', 
             'Z': '√', 'z': '⌂', ' ': 'î', '0': 'ê', '1': 'Æ', '2': '╣', '3': '¥', '4': 'µ', '5': '╠', '6': '¿',
             '7': 'ç', '8': '└', '9': '◘', '!': '§', '*': 'δ', '+': '╧', '-': 'Σ', '/': 'ⁿ', ',': 'Ü', '.': '╕',
             '?': '╫', ':': '▀', ';': '█', '"': '├', "'": '╚', '(': '¡', ')': '╔', '_': 'Ω', '[': '╜', ']': '"',
             '{': '₧', '}': '╓'}
    encrypt(codes)
    decrypt(codes)

        
        
