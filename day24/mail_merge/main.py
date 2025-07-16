with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
for name in names:
    name = name.strip()
    letter = letter_contents.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_file:
        output_file.write(letter)
