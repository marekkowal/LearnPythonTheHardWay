__author__ = 'marek'

def populate_numbers(ceiling, increment):
    i = 0.0
    numbers = []

    while i < ceiling:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

populate_numbers(10, 0.5)