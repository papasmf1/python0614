# ifelse.py
score = int(input("Input Score:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "E"

print("Grade is ", grade)


    
