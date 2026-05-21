import attendance

present = int(input("Classes attended: "))
total = int(input("Total classes: "))

print("Attendance Percentage:",
      attendance.calculate_percentage(present, total))
