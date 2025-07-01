import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            original_position = alphabet.index(letter)
            new_position = (original_position + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
    print(f"Here is the {cipher_direction}d result: {output_text}")

continue_program = True

while continue_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()
    if restart == "no":
        continue_program = False
        print("Thanks for trying the Caesar Cipher.")
