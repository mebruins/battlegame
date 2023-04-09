# Battle Game
import random

# Character damage
def my_damage():
    return random.randint(0,35)

# Dragon damage
def dragon_damage():
    return random.randint(0,50)

# Character heal
def heal():
    return random.randint(10,25)

# start game
while True:
    start = input('Would you like to Battle the Dragon?(Y/N): ')
    if start.lower() == 'y' or start.lower() == 'yes':
        
        while True:
            wizard = "Wizard"
            elf = "Elf"
            human = 'Human'
            orc = 'Orc'
            dragon = 'Dragon'

            # hit points/health
            wizard_hp = 150
            elf_hp = 175
            human_hp = 150
            orc_hp = 250
            dragon_hp = 300



            # Choose avatar
            print('1) Wizard\n2) Elf\n3) Human\n4) Orc')
            character = input('Choose your character: ')
            print('')
            if character == '1' or character.lower() == 'wizard':
                character = wizard
                print('You chose Wizard')
                my_hp = wizard_hp
                print('Your health: ', my_hp)
                print('Dragon health: ', dragon_hp)

            elif character == '2' or character.lower() == 'elf':
                character = elf
                print('You chose Elf')
                my_hp = elf_hp
                print('Your health: ', my_hp)
                print('Dragon health: ', dragon_hp)
                

            elif character == '3' or character.lower() == 'human':
                character = human
                print('You chose Human')
                my_hp = human_hp
                print('Your health: ', my_hp)
                print('Dragon health: ', dragon_hp)
                

            elif character == '4' or character.lower() == 'orc':
                character = orc
                print('You chose Orc')
                my_hp = orc_hp
                print('Your health: ', my_hp)
                print('Dragon health: ', dragon_hp)
                

            else:
                print('Unknown character')
                continue

            # battle or heal?
            while True:
                print('')
                choose = input("Do you wish to (h) heal or (a) attack?")

                # character heal    
                if choose == 'h':
                    my_hp += heal()
                    print("You have healed yourself")
                    print('Your health: ', my_hp)

                # character attack
                elif choose == 'a':
                    dragon_hp = dragon_hp - my_damage()
                    print('The', character, 'damaged the Dragon')
                    print('Dragon health: ', dragon_hp)
                    if dragon_hp <= 0:
                        print('The Dragon has lost the battle!')
                        print('')
                        break
                    
                    # dragon attack
                    my_hp = my_hp - dragon_damage()
                    print('The Dragon has damaged the', character)
                    print('Your health: ', my_hp)
                    if my_hp <= 0:
                        print('The', character, "has lost the battle!")
                        print('')
                        break
                else:
                    print('Please choose (h)heal or (a)attack')
                    continue
            print('')
            break
    
    if start.lower() == 'n' or start.lower() == 'no':
        print('Goodbye!')
        break    
    else:
        print('Please choose (Y/N)')
        continue
          
