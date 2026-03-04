from strength_checker import check_strength
from suggestions import give_suggestions

password = input("Enter password: ")

strength = check_strength(password)

print("\nPassword Strength:", strength)

suggestions = give_suggestions(password)

if suggestions:
    print("\nSuggestions to improve security:")

    for s in suggestions:
        print("-", s)
