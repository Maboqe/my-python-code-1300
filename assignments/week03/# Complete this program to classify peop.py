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
elif age <= 13:
    print ("You are Teenager")
elif age <= 59:
    print ("You are Adult")
else :
    print ("You are Senior")