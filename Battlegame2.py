# Battle Game
import random

# damage

wizard_damage = random.randint(0,75)
elf_damage = random.randint(0,50)
human_damage = random.randint(0,45)
orc_damage = random.randint(0,75)
dragon_damage = random.randint(0,100)

# def my_damage():
#     return random.randint(0,50)

def dragon_damage():
    return random.randint(0,75)


while True:
    wizard = "Wizard"
    elf = "Elf"
    human = 'Human'
    orc = 'Orc'
    dragon = 'Dragon'

    # hit points/health
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 250
    dragon_hp = 300



    while True:
        print('1) Wizard\n2) Elf\n3) Human\n4) Orc')
        character = input('Choose your character: ')

        if character == '1' or character.lower() == 'wizard':
            character = wizard
            print('You chose Wizard')
            my_hp = wizard_hp
            my_damage = wizard_damage
            print('Health: ', my_hp)
            print('Damage: ', my_damage)
            break

        elif character == '2' or character.lower() == 'elf':
            character = elf
            print('You chose Elf')
            my_hp = elf_hp
            my_damage = elf_damage
            print('Health: ', my_hp)
            print('Damage: ', my_damage)
            break

        elif character == '3' or character.lower() == 'human':
            character = human
            print('You chose Human')
            my_hp = human_hp
            my_damage = human_damage
            print('Health: ', my_hp)
            print('Damage: ', my_damage)
            break

        elif character == '4' or character.lower() == 'orc':
            character = orc
            print('You chose Orc')
            my_hp = orc_hp
            my_damage = orc_damage
            print('Health: ', my_hp)
            print('Damage: ', my_damage)
            break

        print('Unknown character')

    # battle
    while True:
        dragon_hp = dragon_hp - my_damage
        print('The', character, 'damaged the Dragon!')
        print('Dragon health: ', dragon_hp)
        if dragon_hp <= 0:
            print('The Dragon has lost the battle!')
            break
        my_hp = my_hp - dragon_damage()
        print('The Dragon has damaged the', character)
        print('Your health: ', my_hp)
        if my_hp <= 0:
            print('The', character, "has lost the battle!")
            break

    # Play again?
    restart = input('Play again?(Y/N): ')
    if restart.lower() == 'n' or restart.lower() == 'no':
        print('Goodbye!')
        break
    elif restart.lower() == 'y' or restart.lower() == 'yes':
        continue
