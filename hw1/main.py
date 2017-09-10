### Author : Linh Phan ###
# CMPE 187 - Software Testing
# Group 15: Branden Caasi, Hedi Moalla, Linh Phan, Josue Ramirez

#Verify Input 
# True = Positive integer
# Reject other type of decimal/floating, negative integer or String/Character type
def checkInput(side):
	#Check if input side length is an positive Int
	try:
		#Convert into int
		if float(side) % 1 != 0:
			print "Decimal / Floating type is not accepted"
			return False	
		value = int(side)
		#Check negative
		if value <= 0:
			print "Negative int is not accepted"
			return False
	#Exception means input is not int
	except ValueError:
		print "Invalid Input. Input MUST be an integer"
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

#Main method that call other functions by order and print output
def main(side1,side2,side3):
	sides = []
	theType = -1
	types = ["Equilateral", "Isosceles", "Scalene"]
	#Checking Input
	if checkInput(side1) and checkInput(side2) and checkInput(side3):
		sides = [int(side1), int(side2),int(side3)]
	else:
		#print "Invalid Input!! Please try again"
		return False
	
	#Checking if a valid triangle
	if checkValidTriangle(sides[0],sides[1],sides[2]):
		#Valid Triangle => What type ?
		theType = checkTriangleType(sides[0],sides[1],sides[2])

	if theType >= 0:
		print "Input = %d / %d / %d ~~~   is a Triangle ~~~  Type = %s" % (sides[0], sides[1], sides[2], types[theType])
	if theType == -1:
		print "Input = %d / %d / %d ~~~  is NOT a Triangle" % (sides[0], sides[1], sides[2])
   
## Main function to be run when execute the code as "python main.py"
if __name__ == '__main__':
	print "*** Running Test cases ***"
	print "Case #1 -> #3, not form triangle"
	main(50,4,4)
	main(4,60,3)
	main(10,20,60)
	
	print "\nCase #4 -> #6, floating/decimal number rejected"
	main(10.1,10,20)
	main(-2.12,3.23,-30)
	main(-1.1,2.2,3.3)
	
	print "\nCase #7 #8, negative integer rejected"
	main(1,-20,3)
	main(-10, -30, 40)
	
	print "\nCase #9, #10, character and String rejected"
	main(10,20,'z')
	main("this is X", 10, "this is Z")
	
	print "\nCase #11, #12: test buffer overflow for int -> bigint converted automatically by Python"
	main(999999999999999999999, 1,1)
	main(99999999999999999999,99999999999999999999,99999999999999999999)

	print "\nCase #13 -> #17, test 3 type of valid triangle"
	main(30,44,55)
	main(22,22,30)
	main(50,44,50)
	main(50,44,44)
	main(555,555,555)

	print "\n\n*** Test end, Pass rate = 100% ***"
