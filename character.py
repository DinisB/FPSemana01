chars = []
count = 3
for i in range(count):
    name = input()
    attack = int(input())
    defense = int(input())
    character =[name, (attack, defense)]
    chars.append(character)

for i in range(count):
    print(str(chars[i][0]))
    print(str(chars[i][1][0]))
    print(str(chars[i][1][1]))
print(chars)
max_attack_chars = chars[0]
max_defense_chars = chars[0]

for character in chars:
    if character[1][0] > max_attack_chars[1][0]:
        max_attack_chars = character
    if character[1][1] > max_defense_chars[1][1]:
        max_defense_chars = character

print("Max ataque é " + max_attack_chars[0] + " com " + str(max_attack_chars[1][0]))
print("Max defesa é" + max_defense_chars[0] + " com " + str(max_defense_chars[1][1]))