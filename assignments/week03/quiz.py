# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if age <= 12:
    print ("You are Child")
elif age <= 19:
    print ("You are Teenager")
elif age <= 59:
    print ("You are Adult")
else :
    print ("You are Senior")



# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print(f"Your balance is {balance} bath")
        elif choice == "2":
            amot = input("Enter Withdraw: ")
            if amot <= 0:
                print("ถอนทำเอี้ยไร 0 bath")
            elif amot > balance:
                print("เงินไม่พอไอนรก")
            else:
                balance - amot
                print("withdraw {balance} bath")