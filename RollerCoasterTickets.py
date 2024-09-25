print("Welcome to the RollerCoaster!")
height = int(input("What is your height in cm? ")

if height >= 120:
    print("You can ride the RollerCoaster")
    age = int(input("What is your age: ")
    if age<= 12:
       bill = 5
       print("Child tickets are $5.")
    elif age <= 18:
       bill = 7
       print("Youth tickets are $7.")
    else:
       bill = 12
       print("Adult tickets are $12.")

     want_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")
    
     if want_photo == "y"
       bill += 3
     print(f"Your total bill is ${bill}")
else:
    print("You are not eligible.")
    
