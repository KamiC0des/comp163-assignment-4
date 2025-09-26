study_options = ["Programming", "Calculus", "English", "History"]

print("\nChoose a subject to study:")
print("Study Options:", study_options)
study_choice = input("Your choice: ")

if study_choice in study_options:
    if study_choice == "Programming" and current_gpa >= 3.0:
        current_gpa += 0.15
        social_points -= 7
        print(f"\nYou chose to study Programming. This improves your GPA, but, since it comes with a lot of assignments, you won't have that much time to socialize!")
    elif study_choice == "Calculus" and not(stress_level < 30):
        current_gpa += 0.1
        social_points -= 2
        print(f"\nStudying Calculus improves your gpa, but slight impacts your social time.")
    elif study_choice == "English" or study_choice == "History":
        current_gpa += 0.05
        social_points += 3
        print(f"\nFocusing on {study_choice} slightly boosts your GPA and allows you time to relax!")
    else:
        print("\nYou studied! No major changes occur this time.")
elif study_choice not in study_options:
    print("\nInvalid subject choice. No changes have been made.")

