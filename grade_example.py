# getting the required input 

student_id = input("Enter student ID: ")
last_name = input("Enter last name: ")
assignment1_mark = int(input("Enter Assignment 1 mark (out of 25): "))
assignment2_mark = int(input("Enter Assignment 2 mark (out of 25): "))
assignment3_mark = int(input("Enter Assignment 3 mark (out of 50): "))

# Calculate total mark
total_mark = assignment1_mark + assignment2_mark + assignment3_mark

# Determine grade based on total mark
if 0 <= total_mark <= 100:
    if 0 <= total_mark < 50:
        grade = "F"
    elif 50 <= total_mark < 65:
        grade = "P"
    elif 65 <= total_mark < 75:
        grade = "C"
    elif 75 <= total_mark < 85:
        grade = "D"
    elif 85 <= total_mark <= 100:
        grade = "HD"
else:
    print(f"Invalid data entry. Total mark must be between 0 and 100. Total = {total_mark}")
    exit()  # This terminates the program

# Display the results
print("\nOutput:")
print(f"   Student ID: {student_id}")
print(f"   Last Name: {last_name}")
print(f"   Total Mark: {total_mark}")
print(f"   Grade: {grade}")
