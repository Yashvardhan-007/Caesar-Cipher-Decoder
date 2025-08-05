from caesar_cipher import caesar_cipher

def main():
    print("=== Caesar Cipher CLI Tool ===")
    choice = input("Do you want to (encode/decode)? ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (0-25): "))

    output = caesar_cipher(message, shift, choice)
    print(f"\nResult: {output}")

if __name__ == "__main__":
    main()
