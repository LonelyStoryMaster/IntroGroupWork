#(1): Prompt for four weights. Add all weights to a list. Output list.
def get_weights():
    weights = []
    for i in range(4):
        weight = float(input("Enter weight %d:\n" % (i + 1)))
        weights.append(weight)
    print("Weights:", weights)
    return weights

#(2): Output average of weights.
def avg_weight(w_list):
    avg = 0
    for x in w_list:
        avg = avg + x
    avg = avg / 4
    print('\nAverage weight: %0.2f' % avg)

#(3): Output max weight from list.
def max_weight(w_list):
    m_weight = max(w_list)
    print('Max weight: %0.2f' % m_weight)
    print()

#(4): Prompt the user for a list index and output that weight in pounds and kilograms.
def lbs_kg(w_list):
    index = int(input('Enter a list index (1 - 4):\n')) - 1
    print('Weight in pounds: %0.2f'% w_list[index])
    print('Weight in kilograms: %0.2f' % (w_list[index]/2.2))
    print()

#(5): Sort the list and output it.
def sort_list(w_list):
    w_list.sort()
    print('Sorted list:', w_list)

def print_weights(w_list):
    avg_weight(w_list)
    max_weight(w_list)
    lbs_kg(w_list)
    sort_list(w_list)

if __name__ == '__main__':
    print_weights(get_weights())
    