def deposit(money):
    try:
        wallet = 1000
        amount = float(money)
        print(f"ยอดเงินเริ่มต้น: {wallet} บาท")
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as Error:
        if str(Error) == "จำนวนเงินฝากต้องมากกว่า 0":
            print(f"\nเกิดข้อผิดพลาด: {Error}")
        else:
            print(f"\nเกิดข้อผิดพลาด: กรุณากรอกตัวเลขเท่านั้น")

    else:
        wallet += amount
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {wallet:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")

print(f"ยอดเงินเริ่มต้น: 1000 บาท")
deposit_money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(deposit_money)