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
def cus_name():
    while True:
        name = str(input("Nhap ten: ")).strip()
        if not name or name.isdigit():
            print("Ten khong hop le, vui long nhap lai: ")
        else:
            return name
def cus_age_main(): #nhap tuoi khach dat phong
    while True:
        try:
            age = int(input("Nhap so tuoi: "))
            if age <18:
                print("Nguoi dat phong can tren 18 tuoi")
            else:
                return age
        except ValueError:
            print("Invalid input, try again")
def cus_num(): #nhap so luong khach bao gom ca nguoi dat phong
    while True:
        try:
            cus_num = int(input("Nhap so luong khach: "))
            if cus_num <1:
                print("Phai co it nhat 1 khach")
            else:
                return cus_num
        except ValueError:
            print("Invalid input, try again")
def cus_age_other(cus_num): #nhap tuoi cua khach con lai khong tinh khach dat phong
    print("Nhap tuoi so khach con lai: ")
    ages=[]
    for i in range (cus_num-1):
        while True:
            try:
                age = int(input(f"Tuoi khach thu {i + 2}: "))
                if age <=0 :
                    print("Vui long nhap lai")
                else:
                    ages.append(age)
                    break
            except ValueError:
                print("Invalid input, try again")
    return ages
def num_room():
    while True:
        try:
            num_room = int(input("Nhap so phong: "))
            if num_room <1:
                print("Phai co toi thieu 1 phong, vui long nhap lai: ")
            else:
                return num_room
        except ValueError:
            print("Invalid input, try again")
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
def main():
    room_type= choose_room_type()
    room_info= room_prices[room_type] #chinh lai hien thi loai phong
    price = get_room_prices(room_type)
    nights = num_stay()
    total_amount = nights*price
    main_name = cus_name()
    main_age = cus_age_main()
    total_guest=cus_num()
    other_ages=cus_age_other(total_guest) if total_guest > 1 else []
    all_ages = [main_age]+other_ages
    print(f"Ten nguoi dat phong: {main_name}")
    print(f"Ban da chon phong: {room_info['name']}")
    print(f"Tong so luot khach va tuoi: {total_guest}")
    print(f'So dem ban da o: {nights}')
    print(f"So khach va tuoi {all_ages}")
    print(f'Tong so tien: {total_amount} USD')
    if payment_process(total_amount):
        print("Dat phong thanh cong")
    else:
        print("Dat phong khong thanh cong")
main()
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