def interval_generator(x, y):
    while x <= y:
        print('1', x, sep=' ')
        yield x
        print('2', x, sep=' ')
        x += 1
        print('3', x, sep=' ')
        yield x
        print('4', x, sep=' ')
        print('hi')


five_to_ten_generator = interval_generator(5, 10)

next(five_to_ten_generator) # 5
print('---')
next(five_to_ten_generator) # 6
print('---')
next(five_to_ten_generator) # hi
print('---')
next(five_to_ten_generator) # hi
print('---')
next(five_to_ten_generator) # 7
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
print('---')
next(five_to_ten_generator) #
