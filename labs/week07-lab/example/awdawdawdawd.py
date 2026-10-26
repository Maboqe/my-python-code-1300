class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private Attribute[cite: 1]
    
    def deposit(self, amount):
        """Method to deposit money"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        """Method to withdraw money"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        elif amount > self.__balance:
            return "Insufficient funds"
        else:
            return "Withdrawal amount must be positive"
    
    def get_balance(self):
        """Method to check balance"""
        return self.__balance
        
    def _set_balance(self, new_balance):
        """Helper to update balance"""
        self.__balance = new_balance


class Interest:
    """Class to calculate interest"""
    def calculate_interest(self, rate):
        return self.get_balance() * rate / 100


class TransactionLogger:
    """Class to log transactions"""
    def log_transaction(self, transaction_type, amount):
        """Method to log transaction type and amount[cite: 3]"""
        print(f"[LOG] Transaction Success: {transaction_type} of {amount} THB")


# คลาส SavingsAccount สืบทอดแบบ Multiple Inheritance
class SavingsAccount(BankAccount, Interest, TransactionLogger):
    
    def __init__(self, account_number, account_holder, initial_balance=0):
        super().__init__(account_number, account_holder, initial_balance)
    
    def withdraw(self, amount):
        """Override เมธอด withdraw โดยห้ามเหลือต่ำกว่า 500 บาท"""
        if amount <= 0:
            return "Withdrawal amount must be positive"
        
        # ตรวจสอบว่าหลังถอนแล้ว ยอดเงินคงเหลือต้องไม่ต่ำกว่า 500
        if self.get_balance() - amount < 500:
            return "Withdrawal denied: Balance cannot fall below 500 THB"
        
        result = super().withdraw(amount)
        if "Withdrew" in result:
            self.log_transaction("Withdraw", amount)
        return result

    def deposit(self, amount):
        result = super().deposit(amount)
        if "Deposited" in result:
            self.log_transaction("Deposit", amount)
        return result

    def add_interest(self, rate):
        """คำนวณและเพิ่มดอกเบี้ยเข้าสู่บัญชี"""
        interest = self.calculate_interest(rate)
        new_balance = self.get_balance() + interest
        self._set_balance(new_balance)
        self.log_transaction("Add Interest", interest)
        return f"Added interest {interest} THB (Rate: {rate}%). New balance: {self.get_balance()} THB"


# ==========================================
# ส่วนโปรแกรมหลัก (Main Program) ตามโจทย์ข้อ 5[cite: 5]
# ==========================================

# สร้างออบเจ็กต์ SavingsAccount[cite: 5]
account = SavingsAccount("1001", "Alice", 5000)

print(f"--- เริ่มต้นระบบบัญชีของ {account.account_holder} ---")
print(f"ยอดเงินเริ่มต้น: {account.get_balance()} บาท\n")

# 1. ฝากเงิน 1,000 บาท[cite: 5]
print("1. ดำเนินการฝากเงิน 1,000 บาท:")
print(account.deposit(1000))
print("-" * 40)

# 2. ถอนเงิน 2,000 บาท[cite: 5]
print("2. ดำเนินการถอนเงิน 2,000 บาท:")
print(account.withdraw(2000))
print("-" * 40)

# 3. ทดลองถอนเงิน 4,000 บาท (ยอดเงินไม่พอ หรือทำให้ต่ำกว่า 500)[cite: 5]
print("3. ทดลองถอนเงิน 4,000 บาท:")
print(account.withdraw(4000))
print("-" * 40)

# 4. คำนวณและเพิ่มดอกเบี้ย 2%[cite: 5]
print("4. คำนวณและเพิ่มดอกเบี้ย 2%:")
print(account.add_interest(2))
print("-" * 40)

# 5. แสดงชื่อเจ้าของบัญชี เลขที่บัญชี และยอดเงินสุดท้าย[cite: 5]
print("5. ข้อมูลสรุปบัญชีสุดท้าย:")
print(f"ชื่อเจ้าของบัญชี: {account.account_holder}")
print(f"เลขที่บัญชี: {account.account_number}")
print(f"ยอดเงินสุดท้าย: {account.get_balance()} บาท")