def sequence_buttons(string):
    symbols = [' ', '.,?!:', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    tanslit = {}

    for symbols, phone in zip(symbols, list(range(10))):
        for i in range(len(symbols)):
            tanslit[ord(symbols[i])] = str(phone) * (i + 1)

    return string.upper().translate(tanslit)


print(sequence_buttons('Hello, World!'))
