from datetime import datetime, date
today = date.today()
#Thay đổi dict để chọn dễ hơn, thay bằng database sau (SQL, MySQL, SQLite,...)
room_prices={
    "1": {"name": "standard", "price": 1},
    "2": {"name": "delux", "price": 5},
    "3": {"name": "suite", "price": 10}
}
def get_room_prices(choice):
    return room_prices[choice]["price"]
def choose_room_type():
    while True:
        for key, info in room_prices.items():
            print(f"{key}. {info['name']} - {info['price']} USD")
        choice = input("Chon loai phong: ").lower()
        if choice in room_prices:
            return choice
        else:
            print("Chon sai con me may roi ngu a, chon lai di cu")
def num_stay():
    while True: #vòng while True để người dùng chọn sai sẽ có cơ hội chọn lại mà không end program
        try:
            number_of_night = int(input("Nhap so dem o: "))
            if number_of_night >= 1:
                print("Tong cong dem o: ", number_of_night)
                return number_of_night
            else:
                print("Vui long nhap lai")
        except ValueError:
            print("vui long nhap lai")
def payment_process(amount):
    while True:
        print(f"so tien can thanh toan: {amount:,} USD")
        choice = input("xac nhan thanh toan (yes/no): ").lower()
        if choice == "yes":
            paid_time = datetime.now().replace(second=0, microsecond=0)
            print("Chuyen thanh toan", paid_time)
            return True
        elif choice == "no":
            print("Thanh toan bi huy")
            return False
        else:
            print("invalid choices")
def testing():
    room_type= choose_room_type()
    price = get_room_prices(room_type)
    nights = num_stay()
    total_amount = nights*price
    print(f"Ban da chon phong: {room_type}")
    print(f'So dem ban da o: {nights}')
    print(f'Tong so tien: {total_amount}')
    if payment_process(total_amount):
        print("Dat phong thanh cong")
    else:
        print("Dat phong khong thanh cong")
testing()
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