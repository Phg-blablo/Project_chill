from datetime import datetime, date
today = date.today()
#Thay đổi dict để chọn dễ hơn, thay bằng database sau (SQL, MySQL, SQLite,...)
room_prices={
    "1": {"name": "standard", "price": 1, "capacity": 2}, #Update thêm capacity phòng
    "2": {"name": "delux", "price": 5, "capacity": 3},
    "3": {"name": "suite", "price": 10, "capacity": 5}
}
def print_room_info(): #In thông tin phòng trước khi điền thông tin
    print("\n ---DANH SÁCH PHÒNG---")
    for info in room_prices.values():
        print(
            f"{info['name']} | "
            f'{info['price']} USD/đêm | '
            f'Tối đa {info['capacity']} khách '
        )

#Điền thông tin
def customer_name(): 
    while True:
        name = input("Nhập tên khách đặt phòng: ").strip()
        if not name or name.isdigit():
            print("Tên không hợp lệ, vui lòng nhập lại")
        else:
            return name
def main_customer_age():
    while True:
        try:
            age = int(input("Nhập tuổi của người đặt phòng: "))
            if age < 18:
                print("Người đặt phòng phải trên 18 tuổi, vui lòng nhập lại")
            else:
                return age
        except ValueError:
            print("Invalid input, try again")
def number_of_customer():
    while True:
        try:
            guest_number = int(input("Vui lòng nhập số lượng khách: "))
            if guest_number < 1:
                print("Phải có ít nhất 1 khách, vui lòng nhập lại")
            else:
                return guest_number
        except ValueError:
            print("Invalid input, try again")
def other_customers_age(total_guest):
    print("Nhập tuổi của các khách còn lại")
    ages = []
    for i in range (total_guest - 1):
        while True:
            try:
                age = int(input(f"Tuổi khách thứ {i + 2}: "))
                if age <= 0:
                    print("Tuổi không hợp lệ, vui lòng nhập lại")
                else:
                    ages.append(age)
                    break
            except ValueError:
                print("Invalid input, try again")
    return ages
def number_of_stay():
    while True: #vòng while True để người dùng chọn sai sẽ có cơ hội chọn lại mà không end program
        try:
            nights = int(input("Nhập số đêm ở dự kiến: "))
            if nights >= 1:
                print("Tổng cộng số đêm ở: ", nights)
                return nights
            else:
                print("Phải có tối thiểu 1 đêm, vui lòng nhập lại")
        except ValueError:
            print("Invalid input, try agian")

#Tổng hợp thông tin đã điền
def collect_guest_info():
    name = customer_name()
    main_age = main_customer_age()
    total_guest = number_of_customer()
    return {
        "name": name,
        "main age": main_age,
        "total_guest": total_guest,
    }
def collect_extra_info():
    other_age = other_customers_age(total_guest) if total_guest > 1 else []
    night = number_of_stay()
    return {
        "other age": other_age,
        "night": night
    }
def available_rooms(total_guest):
    return {
        key: info
        for key, info in room_prices.items()
        if total_guest <= info['capacity']
    }
def select_room(total_guest):
    rooms = available_rooms(total_guest)
    if not rooms:
        return None
    while True:
        print("Các phòng khả dụng")
        for key, info in rooms.items():
            print(f"{key}. {info['name']} - {info['price']} USD - {info['capacity']} khách/phòng")
        choice = input("Chọn phòng: ")
        if choice in rooms:
            return rooms[choice]
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
def payment_process(amount): #Thanh toán
    while True:
        print(f"Số tiền cần thanh toán: {amount:,} USD")
        choice = input("Xác nhận thanh toán (yes/no): ").lower()
        if choice == "yes":
            paid_time = datetime.now().replace(second=0, microsecond=0)
            print("Thanh toán .....", paid_time)
            return True
        elif choice == "no":
            print("Thanh toán bị hủy")
            return False
        else:
            print("invalid choices")
def start_booking():
    guest = collect_guest_info()
    room = select_room(guest['total_guest'])
    if not room:
        print("Không có phòng phù hợp, cảm ơn đã lựa chọn")
        return
    extra_info = collect_extra_info()
    total_amount = guest['night'] * room['price']
    print("\n--- XÁC NHẬN ---")
    print("Tên: ", guest['name'])
    print("Hạng phòng: ", room['name'])
    print("Số khách: ", guest["total_guest"])
    print("Số đêm: ", extra_info["night"])
    print("Tổng số tiền cần thanh toán: ", total_amount, "USD")
    if payment_process(total_amount):
        print("Đặt phòng thành công, cảm ơn đã tin tưởng")
    else:
        print("Đã hủy quá trình đặt phòng, cảm ơn đã lựa chọn")
def main_menu(): #Hàm chạy chính
    while True:
        print("1. Xem phòng")
        print("2. Đặt phòng")
        print("3. Thoát")
        choice = input("Chọn: ")
        if choice == '1':
            print_room_info()
        elif choice == '2':
            start_booking()
        elif choice == '3':
            print("Cảm ơn đã lựa chọn")
        else:
            print("Invalid input, try again")
main_menu()
print(today)

"""
Ăn cắp từ Chat GPT, viết sau đừng để ý

Thay đổi cho user có tùy chọn linh hoạt hơn

from datetime import date, datetime

def get_number_of_nights():
    today = date.today()
    print(f"Ngay hom nay (check-in): {today}")

    while True:
        print("Chon cach nhap:")
        print("1 - Nhap so dem o")
        print("2 - Nhap ngay check-out du kien (YYYY-MM-DD)")

        choice = input("Lua chon cua ban (1/2): ")

        # Cách 1: nhập số đêm
        if choice == "1":
            try:
                nights = int(input("Nhap so dem o: "))
                if nights >= 1:
                    return nights
                else:
                    print("So dem o phai >= 1")
            except ValueError:
                print("Vui long nhap so hop le")

        # Cách 2: nhập ngày checkout
        elif choice == "2":
            checkout_input = input("Nhap ngay check-out (YYYY-MM-DD): ")
            try:
                checkout_date = datetime.strptime(
                    checkout_input, "%Y-%m-%d"
                ).date()

                if checkout_date <= today:
                    print("Ngay check-out phai sau ngay hom nay")
                else:
                    nights = (checkout_date - today).days
                    return nights

            except ValueError:
                print("Sai dinh dang ngay. VD: 2026-01-10")

        else:
            print("Lua chon khong hop le")

"""