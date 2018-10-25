def get_title():
    title = input('Enter a title for the data:\n')
    return title

def get_col1():
    col1= input('Enter the column 1 header:\n')
    return col1
    
def get_col2():    
    col2 = input('Enter the column 2 header:\n')
    return col2

def data_point():
    data = input('Enter a data point (-1 to stop input):\n')
    while data != '-1':
        shit = False
        points = data.split(',')
        
        if ',' not in data:
            print('Error: No comma in string.\n')
        else: 
            if data.count(',') > 1:
                print('Error: Too many commas in input.\n')
            else:
                nums = []
                for i in range(1000):
                    nums.append(str(i))
                if points[1].strip() in nums:
                    shit = True
                else:
                    print('Error: Comma not followed by an integer.\n')
        if shit:
            print('Data string: {}'.format(points[0]))
            print('Data integer:{}\n'.format(points[1]))
        data = input('Enter a data point (-1 to stop input):\n')

if __name__ == '__main__':
    title = get_title()
    print('You entered: %s' % title)
    print()
    col1 = get_col1()
    print('You entered: %s' % col1)
    print()
    col2 = get_col2()
    print('You entered: %s' % col2)
    print()
    data_point()
    print()
    
