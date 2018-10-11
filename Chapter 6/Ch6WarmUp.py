def get_num_of_characters(inputStr):
    char_list = (inputStr)
    num_char = len(char_list)
    return num_char

def output_without_whitespace(inputStr):
    whitespaces = [' ', '\t']
    output = ''
    for ch in inputStr:
        if ch not in whitespaces:
            output += ch
    print("String with no whitespace:", output)

if __name__ =='__main__':
    user_string = input('Enter a sentence or phrase:\n')
    print()
    print('You entered: %s\n' % (user_string))
    print('Number of characters:', get_num_of_characters(user_string))
    output_without_whitespace(user_string)