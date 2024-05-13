
with open("GitProjects\mail-merge\Input\Letters\starting_letter.txt", mode="r") as letter:
    content = letter.read()



with open("GitProjects/mail-merge/Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.read()


for name in name_list.split("\n"):
    new_letter = content.replace("[name]", name)
    with open(f"GitProjects/mail-merge/Output/{name}.txt", mode="w") as file:
        file.write(new_letter)
