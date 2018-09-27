arrow_head_width=0

arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))

print('')
# Draw arrow base (height = 3, width = 2)
i=1
while i <= arrow_base_height:
    print('*' * arrow_base_width)
    i+=1

# Draw arrow head (width = 4)

while arrow_head_width >= 1:
    print('*' * arrow_head_width)
    arrow_head_width -= 1
