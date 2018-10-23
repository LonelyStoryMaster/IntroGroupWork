usr_string = input('Enter input string:\n')

while ',' not in usr_string:
    print('Error: No comma in string.\n')
    usr_string = input('Enter input string:\n')

while usr_string != 'q':
    usr_split = usr_string.split(',')
    usr_split[0] = usr_split[0].strip()
    usr_split[1] = usr_split[1].strip()
    print('First word: {}'.format(usr_split[0]))
    print('Second word: {}\n'.format(usr_split[1]))
    usr_string = input('Enter input string:\n')
