import sys

print("Welcome to this GPA calculator ")
print("A = 4.0 ")
print("B = 3.0 ")
print("C = 2.0 ")
print("D = 1.0 ")
print("F = 0.0 ")
option = input("Options: 1. Normal GPA Calculator/ 2. Cumulative GPA Calculator ")
if option == "1":
  print("You chose the normal GPA Calculator ")
  grades = int(input("Total amount of grade points: "))
  credits = int(input("Total amount of credit hours attempted: "))
  GPA = grades/credits
  if GPA < 5:
    print("Your GPA is: ", GPA)
    sys.exit()
  if GPA > 5:
    print("Your GPA is: ", GPA, "Please check your inputs. ")
    sys.exit()
if option == "2":
  print("You chose the cumulative GPA Calculator ")
  points = int(input("Total amount of grade points in every semester: "))
  hours = int(input("Total amount of credit hours in every semester: "))
  CGPA = points/hours
  if GPA < 5:
    print("Your cumulative GPA is: ", CGPA)
    sys.exit()
  if CGPA > 5.0:
    print("Your GPA is: ", CGPA, "Please check your inputs. " )
    sys.exit()
else:
  print("Error. ")
  sys.exit()
