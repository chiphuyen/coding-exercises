'''
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and
for the multiples of five print “Buzz”. For numbers which are multiples
of both three and five print “FizzBuzz”.
'''


def fizzbuzz():
    results = []
    for i in range(1, 101):
        if i % 15 == 0:
            results.append('fizzbuzz')
        elif i % 3 == 0:
            results.append('fizz')
        elif i % 5 == 0:
            results.append('buzz')
        else:
            results.append(str(i))
    return ' '.join(results)


print(fizzbuzz())
