def main():
    card_number = input("Enter credit card number: ") 
    if check_valid_card(card_number):
        print("Valid credit card number.")
    else:
        print("Invalid credit card number.")

def check_valid_card(n):
    pass

if __name__ == "__main__":
    main()