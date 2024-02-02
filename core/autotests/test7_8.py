def token_parser(s):
    tokens, number = [], ''
    for symbol in s:
        if symbol.isdigit():
            number += symbol
        elif symbol in ['*', '/', '-', '+', '(', ')']:
            if number:
                tokens.append(number)
                number = ''
            tokens.append(symbol)
    if number:
        tokens.append(number)
    return tokens


print(token_parser("2+ 34-5 * 3"))
