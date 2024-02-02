def capital_text(s):
    symbols = ['.', ',', '?', '!']
    s = s.strip().capitalize()
    indexes_to_replace = []
    skip = False

    for i, char in enumerate(s):
        if skip:
            skip = False
            continue
        if char in symbols:
            skip = True
            for j in range(i + 1, len(s)):
                if s[j].isspace():
                    continue
                indexes_to_replace.append(j)
                break

    text_list = list(s)
    for index in indexes_to_replace:
        text_list[index] = text_list[index].upper()

    return ''.join(text_list)

