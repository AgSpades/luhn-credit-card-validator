
def main():
    card_number = input("Enter credit card number: ").strip()
    if is_valid_card(card_number):
        print("Valid credit card number.")
    else:
        print("Invalid credit card number.")

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
        
    return checksum % 10 == 0

def is_valid_card(card_number):
    if not card_number.isdigit() or len(card_number) < 15:
        return False
    return luhn_check(card_number)

if __name__ == "__main__":
    main()