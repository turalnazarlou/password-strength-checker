import string

def check_password(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")
        
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")
    
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")
    
    
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

password = input("Enter your password: ")

result = check_password(password)

print("\nPassword strength: ", result["strength"])

print("\nScore: ", result["score"])

if result["feedback"]:
    print("\nRecommendations:")
    for suggestion in result["feedback"]:
        print("-", suggestion)
else:
    print("\nYour password meets all basic checks!")