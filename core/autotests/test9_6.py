import re


def generator_numbers(string=""):
    matches = re.finditer(r'\d+', string)
    for match in matches:
        yield match.group()


def sum_profit(string):
    profit = 0
    for number in generator_numbers(string):
        profit += int(number)
    return profit


def main():
    str = "Th10e resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
    profit = sum_profit(str)
    print(f'Profit: {profit}')
    pass


if __name__ == '__main__':
    main()
