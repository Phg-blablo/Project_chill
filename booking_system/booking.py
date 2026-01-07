from datetime import datetime

room_prices={
    "standard":1,
    "delux":3,
    "suite":5.5
}
def get_room_prices(room_type):
    return room_prices.get(room_type)
def list_room_prices():
    return room_prices.items()
def choose_room_type():
    while True:
        for room, price in list_room_prices():
            print(f"{room}: {price}")
        choice = input("Chon loai phong: ").lower()
        if choice in room_prices:
            return choice
        else:
            print("Chon sai con me may roi ngu a, chon lai di cu")
def num_stay():
    while True: 
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
            print("Chuyen thanh toan")
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