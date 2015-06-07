students = [["Ben", {"Maths": 67, "English": 78, "Science": 72}],
	    ["Mark", {"Maths": 56, "Art": 64, "History": 39, "Geography": 55}],
	    ["Paul", {"English": 66, "History": 88}]]

grades = ((0, "FAIL"),(50, "D"),(60, "C"),(70, "B"),(80, "A"),(101, "CHEAT!"))

def print_report_card(report_student=None):
	for student in students:
		if ((student[0] == report_student) or
		   (report_student == None)):
			print("Report card for student ", student[0])
			for subject, mark in student[1].items():
				for grade in grades:
					if mark < grade[0]:
						print(subject, ":", prev_grade)
						break
					prev_grade = grade[1]			
				
def add_student(student_name):
	global students
	for student in students:
		if student[0] == student_name:
			return "Student already in database"
	students.append([student_name, {}])
	return "Student added successfully"

def add_mark(student_name, subject, mark):
	global students
	for student in students:
		if student[0] == student_name:
			if subject in student[1].keys():
				print(student_name, " already has a mark for ", subject)
				user_input = input("Overwrite Y/N? ")
				if (user_input == "Y") or (user_input == "y"):
					student[1][subject] = mark
					return "Student's mark updated"
				else:
					return "Student's mark not updated"
			else:
				student[1][subject] = mark
				return "Student's mark added"
	return "Student not found"

while True:
	print("Welcome to the Raspberry Pi student database")
	print("What can I help you with?")
	print("Enter 1 to view all report cards")
	print("Enter 2 to view the report card for a student")
	print("Enter 3 to add a student")
	print("Enter 4 to add a mark to a student")
	print("Enter 5 to exit")
	
	try:
		user_choice = int(input("Choice: "))
	except ValueError:
		print("That is not a number that I recognize")
		user_choice = 0
	
	if user_choice == 1:
		print_report_card()
	elif user_choice == 2:
		enter_student = input("Which student? ")
		print_report_card(enter_student)
	elif user_choice == 3:
		enter_student = input("Student name? ")
		print(add_student(enter_student))
	elif user_choice == 4:
		enter_student = input("Student name? ")
		enter_subject = input("Subject? ")
		num_error = True
		while num_error:
			num_error = False
			try:
				enter_mark = int(input("Mark? "))
			except ValueError:
				print("I don't recognize that as a number")
				num_error = True
		print(add_mark(enter_student, enter_subject, enter_mark))
	elif user_choice == 5:
		break
	else:
		print("Unknown choice")
	input("Press enter to continue")

print("Goodbye and thanks for using the Raspberry Pi Student database")
