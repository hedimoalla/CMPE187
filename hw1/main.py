#Verify Input
def checkInput(side):
	#Check if input side length is an positive Int
	try:
		#Convert into int	
		value = int(side)
		#Check negative
		if val < 0:
			print "Negative int is not accepted"
			return False
	#Exception means input is not int
	except ValueError:
		print "Input is not integer"
		return False

	return True

#Check if 3 side can form a triangle
def checkValidTriangle(side1,side2,side3):
	if (side1>=side2+side3) or (side2>=side1+side3) or (side3>=side1+side2):
		return False
	else:
		return True

#Check Triangle Type:
# Type 0 = Equilateral
# Type 1 = Isosceles
# Type 2 = Scalene
def checkTriangleType(side1,side2,side3):
	if (side1 == side2) and (side2==side3) and (side3==side1):
		return 0
	elif ((side1 == side2) and (side1 != side3) and (side2!=side3)) \
	 or ((side1==side3) and (side1!=side2) and (side2!=side3)) \
	 or ((side2==side3) and (side1!=side2) and (side1!=side3)):
		return 1
	else: 
		return 2



