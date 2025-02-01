age = int(input("Please enter your age: "))

if age < 13:
    print("You can see G rated movies.")
elif 13 <= age <= 17:
    print("You can see PG-13 rated movies.")
else:
    print("You can see R rated movies.")

