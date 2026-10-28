"""
programming => การเขียนโปรแกรม
2 types
1) structured programming ==> การเขียนโปรแกรมเชิงโครงสร้าง ==> C, JS, PHP, Python
2) Object-Oriented Programming ==> การเขียนโปรแกรมเชิงวัตถุ ==> Java, C#, Python
"""

# วิธีการ หรือแนวทางการแก้ปัญหา  template/แม่แบบ/พิมพ์เขียว/ตรายาง
class ClassName:
    """Class docstring"""

    # ข้อมูลที่จำเป็นในการแก้ปัญหา
    def __init__(self, value, value2, value3):
        self.attribute = value
        self.attribute2 = value2
        self.attribute3 = value3

    # การกระทำเพื่อแก้ปัญหา
    def method_name(self):
        return self.attribute

    def method_name2(self):
        return self.attribute2


# สร้างวัตถุจาก Class
myObj = ClassName("Hello", 10, 20)

# แสดงข้อมูล
print(myObj.attribute)

# เรียกใช้งาน Method
resultFromMethod = myObj.method_name()
print(resultFromMethod)

print(myObj.method_name2())