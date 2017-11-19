'''
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and 
for the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.
'''
def fizzbuzz():
	results = ''
	for i in range(100):
		if (i + 1) % 15 == 0:
			results += 'fizzbuzz'
		elif (i + 1) % 3 == 0:
			results += 'fizz'
		elif (i + 1) % 5 == 0:
			results += 'buzz'
		else:
			results += ' '
	return results

print(fizzbuzz())

