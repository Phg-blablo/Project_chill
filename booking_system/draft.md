from datetime import datetime

# =========================
# ROOM & PRICING
# =========================

ROOM_PRICES = {
    "standard": 500_000,
    "deluxe": 800_000,
    "suite": 1_200_000
}

def get_room_price(room_type):
    return ROOM_PRICES.get(room_type)


# =========================
# DATE LOGIC
# =========================

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def calculate_nights(check_in, check_out):
    return (check_out - check_in).days


# =========================
# PAYMENT (MOCK)
# =========================

def process_payment(amount):
    print(f"Số tiền cần thanh toán: {amount:,} VND")
    return input("Xác nhận thanh toán? (yes/no): ").lower() == "yes"


# =========================
# BOOKING
# =========================

def calculate_total_price(room_type, nights):
    price = get_room_price(room_type)
    if price is None:
        raise ValueError("Invalid room type")
    return price * nights


def confirm_booking(booking):
    print("\n=== XÁC NHẬN ĐẶT PHÒNG ===")
    for k, v in booking.items():
        print(f"{k}: {v}")
    print("Đặt phòng thành công ✅")


# =========================
# CORE WORKFLOW
# =========================

def run_booking_flow():
    print("Các hạng phòng:")
    for room, price in ROOM_PRICES.items():
        print(f"- {room}: {price:,} VND/đêm")

    room_type = input("Chọn hạng phòng: ")
    check_in = parse_date(input("Check-in (YYYY-MM-DD): "))
    check_out = parse_date(input("Check-out (YYYY-MM-DD): "))

    nights = calculate_nights(check_in, check_out)
    if nights <= 0:
        print("Ngày không hợp lệ ❌")
        return

    total_price = calculate_total_price(room_type, nights)

    if not process_payment(total_price):
        print("Thanh toán thất bại ❌")
        return

    booking = {
        "room_type": room_type,
        "check_in": check_in.date(),
        "check_out": check_out.date(),
        "nights": nights,
        "total_price": total_price
    }

    confirm_booking(booking)
