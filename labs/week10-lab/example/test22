# ===========================
# 7. ITERATING AND COUNTING
# ===========================
# เขียนโปรแกรม นับจำนวนอักขระที่สนใจในข้อความที่กำหนดโดยผู้ใช้งาน
# 1.รับข้อความที่กำหนดให้ผู้ใช้ (text)
# 2.รับอักขระที่สนใจจากผู้ใช้งาน (char)
# 3.แสดงผลการนับอักขระที่สนใจในข้อความออกทางด้านหน้า

#ตัวอย่างหน้าจอ
#Insert the text: Kasetsart Sriracha
#Character to find: r
#3 letters 'r' fond in 'Kasetsart Shiracha'
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text: ")
char = input("Character to find; ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

# เขียนโปรแกรม ตรวจสอบความแข็งแรงของ password
# password ที่แข็งแรงคือ ยาวมากกว่า 8 ตัว และ ผสมกันระหว่างตัวเลข ตัวอักษร และอักขระพิเศษ

# ตัวอย่างหน้าจอ
# Insert your password: Test123
# Your password is not strong!

# Insert your password: Test1234
# Your password is strong!

password = input("Enter Your Password: ")

have_letter = any(gpt.isalpha() for gpt in password)
have_digit = any(gpt.isdigit() for gpt in password)
have_salnum = any(gpt.isalnum() for gpt in password)

if len(password) >= 8 and have_letter and have_digit and have_salnum:
    print("Your password is strong!")
else:
    print("Your password is not strong!")