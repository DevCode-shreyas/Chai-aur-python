password = input("Enter your password: ")


if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "medium"
else:
    strength = "strong"

print(f"Your password is {strength}.")