def distance():
	x1 = input("x1: ")
	x2 = input("x2: ")
	y1 = input("y1: ")
	y2 = input("y2: ")
	x3 = int(x1) - int(x2)
	y3 = int(y1) - int(y2)
	x3 = x3**2
	y3 = y3**2
	toSquare = x3+y3
	print(toSquare**0.5)
	recurse = input("Repeat>\n y/n> ")
	if recurse == "y":
		return distance()
	return

distance()