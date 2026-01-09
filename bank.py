import sys

def safe_int(v, d):
    try:
        return int(v)
    except:
        return d


def safe_str(v, d):
    if v.strip() == "":
        return d
    return v


if len(sys.argv) == 6:
    script = sys.argv[0]
    name = safe_str(sys.argv[1], "Unknown")
    account_no = safe_int(sys.argv[2], 1111111111)
    bank = safe_str(sys.argv[3], "Unknown Bank")
    city = safe_str(sys.argv[4], "Unknown City")
    account_type = safe_str(sys.argv[5], "auto")
    print("user provided input values:")
else:
    script = sys.argv[0]
    name = "Soumya"
    account_no = 1234567890
    bank = "SBI"
    city = "Hubballi"
    account_type = "auto"
    print("no input given - using default values:")


if account_type == "auto":
    if city.lower() == "hubballi":
        account_status = "Local Bank Account"
    else:
        account_status = "Non-Local Bank Account"
else:
    account_status = account_type


print("\n--- Bank Details Result ---")
print("script name :", script)
print("name :", name)
print("account no :", account_no)
print("bank :", bank)
print("city :", city)
print("account status :", account_status)