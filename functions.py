def centered_text(*args, sep=' '):
    text = ''
    for arg in args:
        text += str(arg) + sep
    shift = (60 - len(text)) // 2
    return ' ' * shift + text


#with open('centered', 'w') as centered_output:

# str_1 = centered_text('Hello', 'You', 1, 2, 3)
# print(str_1)
# str_2 = centered_text('World is here', 1, 3, 5, 6, 7)
# print(str_2)

with open('centered_1', 'w') as menu:
    str_1 = centered_text('Hello', 'You', 1, 2, 3)
    print(str_1, file=menu)
    str_2 = centered_text('World is here', 1, 3, 5, 6, 7)
    print(str_2, file=menu)
    print(centered_text('I have a little valentine', 'It someone sent to me', 12), file=menu)
    print(centered_text('When I was Just a little boy!', sep=':'), file=menu)
