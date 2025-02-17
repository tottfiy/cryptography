def ceasar():
    while True:
        mode = input("Enter encryption (1) or decryption (2) mode: ")
        if mode in ('1', '2'):
            break
        print("Invalid input. Please enter 1 or 2.")

    shift = 5 if mode == '1' else -5
    input_text = input("Enter your message: ")
    output_text = ''
    for letter in input_text:
        letter = letter.lower()
        c = ord(letter) + shift
        if c > 122:
            c -= 26
        elif c < 97:
            c += 26
        output_text += chr(c)
    print(output_text)


def tritemius():
    while True:
        mode = input("Enter encryption (1) or decryption (2) mode: ")
        if mode in ('1', '2'):
            break
        print("Invalid input. Please enter 1 or 2.")

    input_text = input("Enter your message: ")
    code_text = 'jpegmafia'
    output_text = ''
    i = 0
    for x in input_text:
        if i >= len(code_text):
            i = 0
        x = x.lower()
        if x == ' ':
            output_text += ' '
        else:
            shift = ord(code_text[i]) - 97
            c = ord(x) + shift if mode == '1' else ord(x) - shift
            if c > 122:
                c -= 26
            elif c < 97:
                c += 26
            output_text += chr(c)
            i += 1
    print(output_text)


ceasar()
tritemius()
