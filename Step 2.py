print("\nChoose your course load:")
print("A) Light Load (12 credits)")
print("B) Standard Load (15 credits)")
print("C) Heavy Load (18 credits)")
choice = input("Your choice: ")

if choice == "A":
    if current_gpa >= 2.5:
        study_hours += 4
        stress_level -= 10
        print(f"You chose option A: 'Light Load'. With your GPA, this should be easy! You should study {study_hours} hours. Your stress level will go down to {stress_level}. ")
    else:
        study_hours += 6
        stress_level -= 5
        print(f"You chose option A: 'Light Load'. This gives you time to improve your GPA! You should study {study_hours} hours. Your stress level will go down to {stress_level}.")
elif choice == "B":
    if current_gpa >= 3.0:
        study_hours += 7
        stress_level += 5
        print(f"You chose option B: 'Standard Load'. Balanced, but will still cause a little stress. You should study {study_hours} hours. Your stress level will go up to {stress_level}.")
    else:
        study_hours += 9
        stress_level += 8
        print(f"You chose option B: 'Standard Load'. This might be a little tough with your GPA. You should study {study_hours} hours. Your stress level will go up to {stress_level}.")

elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 10
        stress_level += 10
        print(f"You chose option C : 'Heavy Load'. You should study {study_hours} hours. Your stress level will go up to {stress_level}. You can handle this with your GPA!")
    else:
        study_hours += 16
        stress_level += 20
        print(
            f"You chose option C : 'Heavy Load'. You should study {study_hours} hours. Your stress level will go up to {stress_level}. This will overwhelm you with your GPA...")
else:
    print("Invalid choice.")