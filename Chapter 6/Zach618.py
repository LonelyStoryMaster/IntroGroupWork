def get_num_of_characters(inputStr):
    char_list = (inputStr)
    num_char = len(char_list)
    return num_char

def output_without_white_space(the_string):
    no_space = ''
    for x in the_string:
            if x != ' ':
                no_space += x
    return no_space
            
if __name__ == '__main__':
    user_string = input('Enter a sentence or phrase:\n')
    print()
    print('You entered: %s\n' % (user_string))
    print('Number of characters:', get_num_of_characters(user_string))
    print('String with no whitespace:', output_without_white_space(user_string))
    
