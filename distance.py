def distance(x1, x2, y1, y2):
	x3 = int(x1) - int(x2)
	y3 = int(y1) - int(y2)
	x3 = x3**2
	y3 = y3**2
	distance = (x3+y3)**0.5
	return distance
