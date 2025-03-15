    
         


def check_password_strength(password):
    strength = "Weak"
    feedback = []

    if len(password) >= 8:
        strength = "Medium"
        feedback.append("Password length is sufficient.")
    else:
        feedback.append("Password length should be at least 8 characters.")

    if any(char.isdigit() for char in password):
        if strength == "Medium":
            strength = "Strong"
           
    else:
        feedback.append("Password should contain at least one number.")

    if any(char.isupper() for char in password):
        if strength == "Strong":
            strength = "Very Strong"
        
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if any(not char.isalnum() for char in password):
        if strength == "Very Strong":
            strength = "Extremely Strong"
     
    else:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback



