def get_num_of_characters(inputStr):
    return len(inputStr)

def output_without_whitespace(inputStr):
    whitespaces = [' ', '\t']
    output = ''
    for ch in inputStr:
        if ch not in whitespaces:
            output += ch
    print("String with no whitespace:", output)

if __name__ == '__main__':
    # Type your code here
    user_input = input("Enter a sentence or phrase:\n")
    print("\nYou entered:", user_input)
    print('\nNumber of characters:', get_num_of_characters(user_input))
    output_without_whitespace(user_input)
    