import re

def assess_password_strength(password):
    score = 0
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'\d', password)
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_criteria:
        score += 1
    feedback = []
    
    if length_criteria:
        feedback.append("Good: Password length is sufficient.")
    else:
        feedback.append("Weak: Password should be at least 8 characters long.")
    
    if uppercase_criteria:
        feedback.append("Good: Password contains uppercase letters.")
    else:
        feedback.append("Weak: Password should contain at least one uppercase letter.")
    
    if lowercase_criteria:
        feedback.append("Good: Password contains lowercase letters.")
    else:
        feedback.append("Weak: Password should contain at least one lowercase letter.")
    
    if number_criteria:
        feedback.append("Good: Password contains numbers.")
    else:
        feedback.append("Weak: Password should contain at least one number.")
    
    if special_criteria:
        feedback.append("Good: Password contains special characters.")
    else:
        feedback.append("Weak: Password should contain at least one special character.")
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, feedback
password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
for comment in feedback:
    print(comment)