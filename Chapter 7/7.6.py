def fuckingStop():
    #WE DONE HERE
    pass

def split_string(user_str):
    usr_split = user_str.split(',')
    usr_split[0] = usr_split[0].strip()
    usr_split[1] = usr_split[1].strip()
    return usr_split

def get_string(usr_string):
    while ',' not in usr_string:
        print('Error: No comma in string.\n')
        usr_string = input('Enter input string:\n')
    return usr_string

def print_the_stuffs(string_list):
    print('First word: {}'.format(string_list[0]))
    print('Second word: {}\n'.format(string_list[1]))

if __name__ == '__main__':
    user_string = input("Enter input string:\n")
    while user_string != 'q':
        string = get_string(user_string)
        string_list = split_string(string)
        print_the_stuffs(string_list)
        user_string = input("Enter input string:\n")
    else:
        fuckingStop()