#Verify Input
def checkInput(side):
	#Check if input side length is an positive Int
	try:
		#Convert into int	
		value = int(side)
		#Check negative
		if value < 0:
			print "Negative int is not accepted"
			return False
	#Exception means input is not int
	except ValueError:
		print "Input is not integer"
		return False
	#If none exception => The input is Integer
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
	#Type 0 == Equilateral
	if (side1 == side2) and (side2==side3) and (side3==side1):
		return 0
	#Type 1 == Isosceles
	elif ((side1 == side2) and (side1 != side3) and (side2!=side3)) \
	 or ((side1==side3) and (side1!=side2) and (side2!=side3)) \
	 or ((side2==side3) and (side1!=side2) and (side1!=side3)):
		return 1
	#Type 2 == Scalene
	else: 
		return 2


def main(side1,side2,side3):
	sides = []
	theType = -1
	types = ["Equilateral", "Isosceles", "Scalene"]
	#Checking Input
	if checkInput(side1) and checkInput(side2) and checkInput(side3):
		sides = [int(side1), int(side2),int(side3)]
	else:
		print "Invalid Input!! Please try again"
		return False
	
	#Checking if a valid triangle
	if checkValidTriangle(sides[0],sides[1],sides[2]):
		#Valid Triangle => What type ?
		theType = checkTriangleType(sides[0],sides[1],sides[2])
	
	if theType >= 0:
		print "Triangle Length = %d / %d / %d ~~~  Is Triangle ? - True ~~  Type = %s" % (sides[0], sides[1], sides[2], types[theType])
	if theType == -1:
		print "Triangle Length = %d / %d / %d ~~~  Is Triangle ? - False" % (sides[0], sides[1], sides[2])
   
if __name__ == '__main__':
	print "*** Testing 3 different cases ***"
	main(30,44,55)
	main(50,44,44)
	main(555,555,555)
	main(50,4,4)

	print "\n*** Testing exception ***"
	print "Negative and non-int.."
	main(-11,22,33)
	#main(-122,-22,334)
	main("Some random word", 123,123)
	#main(8.123, 12.111111,11.22)

