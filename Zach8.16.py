def weights():
    weight= []
    for x in range(4):
        weight.append(float(input('Enter weight %d:\n' % (x+1))))
    print('Weights:', weight)
    print()
    return weight


def avg_weight(w_list):
    avg = 0
    for x in w_list:
        avg = avg + x
    avg = avg / 4
    print('Average weight: %0.2f' % avg)


def max_weight(w_list):
    m_weight = max(w_list)
    print('Max weight: %0.2f' % m_weight)
    print()


def lbs_kg(w_list):
    index = int(input('Enter a list index (1 - 4):\n')) - 1
    print('Weight in pounds: %0.2f'% w_list[index])
    print('Weight in kilograms: %0.2f' % (w_list[index]/2.2))
    print()


def sort_list(w_list):
    w_list.sort()
    print('Sorted list:', w_list)


if __name__ == '__main__':
    var = weights()
    avg_weight(var)
    max_weight(var)
    lbs_kg(var)
    sort_list(var)
