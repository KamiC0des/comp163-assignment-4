print("\n==== FINAL SEMESTER ASSESSMENT ====")

if (type(current_gpa) is float) and (type(study_hours) is int) and (type(social_points) is int) and (type(stress_level) is int):
    print("Type check passed! GPA is a float, study hours is an integer, social points is an integer, and stress level is an integer")
elif (type(current_gpa) is not float) or (type(study_hours) is not int) or (type(social_points) is not int) or (type(stress_level) is not int):
    print("Type check failed. Something went wrong with the variable types.")

if current_gpa >= 3.5:
    ending = "Great Job! Keep Up The Good Work."
    if stress_level <= 50:
        stats = "Dean's List! You had outstanding grades this semester with a great balance, Congrats!"
    else:
        stats = "You had outstanding grades this semester, but you nearly burned out."
elif current_gpa >= 2.7:
    ending = "Good! There's Room For Improvement."
    if stress_level <= 50 and social_points >= 45:
        stats = "You maintained pretty solid grades while still having fun and being stress-free, Congrats!"
    else:
        stats = "You had a pretty good semester, but you struggled with balance between stress, fun, and work. "
else:
    ending = "Try Harder Next Semester!"
    if stress_level >= 55 or social_points <= 30:
        stats = "You had a rough semester - grades dropped and you burned out."
    else:
        stats = "You had a rough semester, but you survived! Improvement is needed next semester."

print("\n---- Final Outcome ----")
print(stats)

print(f"\n---- {student_name}'s Final Stats ----")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}/100")
print(f"\n{ending}")
print("=================================================")
