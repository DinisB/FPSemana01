chars = []
count = 3
for i in range(count):
    name = input("Name the character")
    attack = int(input("Insert attack stats"))
    defense = int(input("Insert defense stats"))
    character =[name, (attack, defense)]
    chars.append(character)
    print("Nome " + str(chars[i][0]) + " Ataque " + str(chars[i][1][0]) + " Defesa " + str(chars[i][1][1]))