pet = input("Enter a pet: ")
pet_age = int(input("Enter the age of the pet: "))

if pet == "Dog":
    if pet_age <2:
        print("Puppy Food")
    else:
        print("Adult Dog Food")
elif pet == "Cat":
    if pet_age >5:
        print("Senior Cat Food")
    else:

