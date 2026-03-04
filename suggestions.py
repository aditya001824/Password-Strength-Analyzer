def give_suggestions(password):

    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters")

    if not any(char.isupper() for char in password):
        suggestions.append("Add uppercase letters")

    if not any(char.islower() for char in password):
        suggestions.append("Add lowercase letters")

    if not any(char.isdigit() for char in password):
        suggestions.append("Add numbers")

    if not any(char in "!@#$%^&*" for char in password):
        suggestions.append("Add special characters")

    return suggestions
