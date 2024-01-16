# Program to find the average grade of 3 marks
maths = int(input("Enter your grade in Maths (/100): "))
science = int(input("Enter your grade in Science (/100): "))
sst = int(input("Enter your grade in SST (/100): "))

average_grade = (maths + science + sst) / 3
print("Your grade is: ", end='') # We use end='' so that the grade prints side by side

if 91 <= average_grade <= 100: print("A1")
elif 81 <= average_grade <= 90: print("A2")
elif 71 <= average_grade <= 80: print("B1")
elif 61 <= average_grade <= 70: print("B2")
elif 51 <= average_grade <= 60: print("C1")
elif 41 <= average_grade <= 50: print("C2")
elif 33 <= average_grade <= 40: print("D")
elif 21 <= average_grade <= 32: print("E1")
elif 0 <= average_grade <= 20: print("E2")

