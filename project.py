def main():
    print_welcome()
    name = input("اسم شما چیه؟ ").strip()
    age = get_age()
    days = calculate_days_lived(age)
    print(f"\nسلام {name} جان!")
    print(f"تو تا الان تقریباً {days:,} روز زندگی کردی!")
    print("عجب زندگی قشنگی!")


def print_welcome():
    print("\n" + "=" * 55)
    print("    خوش اومدی به محاسبه‌گر روزهای زندگی!")
    print("           CS50x Iran - پروژه نهایی")
    print("=" * 55 + "\n")


def get_age():
    while True:
        try:
            age = int(input("چند سالته؟ "))
            if 1 <= age <= 150:
                return age
            else:
                print("سن باید بین ۱ تا ۱۵۰ سال باشه!")
        except ValueError:
            print("لطفاً فقط عدد وارد کن!")


def calculate_days_lived(age):
    """محاسبه تقریبی روزهای زندگی با در نظر گرفتن سال کبیسه"""
    return age * 365 + (age // 4)  # هر ۴ سال یک روز اضافه


if __name__ == "__main__":
    main()
