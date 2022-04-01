# sabiranje
def add(x, y):
    return (x+y)

# oduzimanje
def subtract(x,y):
    return(x-y)

# množenje
def multiply(x,y):
    return(x*y)

# dijeljenje
def divide(x,y):
    return(x/y)

# Unesite prvi broj
no1=eval(input("Enter the first number: "))

# Unesite drugi broj
no2= eval(input("Enter the second number: "))

# prikaz opcija na display
print("Select the option")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

# radnja se ponavlja
while(True):
    # Korisnik bira opcije
    choice=int(input("Enter the choice from (1/2/3/4/5" ))
    # ako je opcija 1,2,3,4,5 true će se izvršiti, u suprotnom prikazati poruka "Invalid choice try again"
    if choice in (1,2,3,4,5):
        if choice == 1:
            print("Addition of two number", no1, "and ",no2, "is: ",add(no1,no2))
        elif choice == 2:
            print("Subtraction of two number", no1, "and ",no2, "is: ",subtract(no1,no2))
        elif choice == 3:
            print("Subtraction of two number", no1, "and ",no2, "is: ",multiply(no1,no2))
        elif choice == 4:
            print("Subtraction of two number", no1, "and ",no2, "is: ",divide(no1,no2))
        elif choice == 5:
            print("Thank you :")
    else:
        print("Invalid choice try again")



