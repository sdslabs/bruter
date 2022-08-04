from bruter import brute

def printer(x):
	print(x)

symbols = {
	'H': ['a', 'b', 'c'],
	'L': ['x', 'y'],
	'X': ['1', '2']
}

brute("hello <H> <L> <X>", printer, symbols)
