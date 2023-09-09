'''
Module to make heroes and monster interact to each other, as the main purpose of the game
'''

import random
import time
from .Character import *
from .Hero import *
from .Monster import *


def stat(team, monster):
    '''
    Function for showing character's status
    '''
    print("==================================")
    for member in team:
        if (member.energy < member.max_energy) and (member.energy >= 0):
            print(f"{member.name}'s HP : {member.hp} // Energy : {member.energy} // Attack : {member.curr_base_atk}")
        else:
            print(f"{member.name}'s HP : {member.hp} // Energy : {member.energy} (max) // Attack : {member.curr_base_atk}")
    print("==================================")
    if (monster.energy < monster.max_energy) and (monster.energy >= 0):
        print(f"{monster.name}'s HP : {monster.hp} // Energy : {monster.energy} // Attack : {monster.curr_base_atk}")
    else:
        print(f"{monster.name}'s HP : {monster.hp} // Energy : {monster.energy} (max) // Attack : {monster.curr_base_atk}")
    print("==================================")


def team_action(team,member,warrior,ranger,cleric,shaman,monster):
    '''
    Function for controlling the action of the team.
    The team consist of four member: warrior, ranger, cleric and shaman.
    '''
    while(True):
        #take user's input for hero's actions
        action = input(f"\n{member.name}'s turn \n1. Normal Attack\n2. Skill\n3. Ultimate\nChoose your action: ")
        
        #match the input user to the available actions
        match action:
            case "1": member.normal_atk(monster); break 
            case "2":
                if not member.energy >= 20:
                    print("Insufficient energy")
                    time.sleep(1)
                else:
                    if member == cleric:
                        print(f"Choose your ally to heal :\n1. {warrior.name}\n2. {ranger.name}\n3. {cleric.name}\n4. {shaman.name}\n Your choice: ")
                        skill_target(member,warrior,ranger,cleric,shaman)
                        break
                    elif member == shaman:
                        print(f"Choose your ally to increase the attack :\n1. {warrior.name}\n2. {ranger.name}\n3. {cleric.name}\n4. {shaman.name}\n Your choice: ")
                        skill_target(member,warrior,ranger,cleric,shaman)
                        break
                    else:
                        member.skill(monster)
                        break
            case "3":
                if member.energy != member.max_energy:
                    print("Insufficient energy")
                    time.sleep(1)
                else:
                    if member == cleric:
                        print(f"{member.name} using ultimate skill to all allies")
                        time.sleep(1)
                        allmember = [member for member in team if member.is_alive()]
                        for item in allmember:
                            member.ultimate(item)
                        print(f"all allies has been healed by {int(0.5 * member.max_hp)}")
                        time.sleep(1)
                        break
                    elif member == shaman:
                        ally = input(f"Choose your ally to charge his/her energy :\n1. {warrior.name}\n2. {ranger.name}\n3. {cleric.name}\n4. {shaman.name}\n Your choice: ")
                        match ally:
                            case "1":member.ultimate(warrior)
                            case "2":member.ultimate(ranger)
                            case "3":member.ultimate(cleric)
                            case "4":member.ultimate(shaman)
                        break
                    else:
                        member.ultimate(monster)
                        break
            case _: 
                print("Invalid input")
                time.sleep(1)
                            

def monster_action(monster,available_target):
    '''
    Function for controlling the monster's action.
    '''
    decision = random.randint(0,1) 
    if decision == 0:
        if monster.energy >= 20:
            monster.skill(random.choice(available_target),random.choice(available_target),random.choice(available_target),random.choice(available_target))
        elif (monster.energy >= 20) and (monster.hp < (0.5 * monster.max_hp)):
            monster.heal()
        elif monster.energy == monster.max_energy:
            print(f"{monster.name} is using ultimate skill")
            time.sleep(1)
            for item in available_target:
                monster.ultimate(item)
            monster.energy_regen()
    else:
        monster.normal_atk(random.choice(available_target),random.choice(available_target))
    

def skill_target(member,warrior,ranger,cleric,shaman):
    '''
    Function for targeting the member of the team to take the effect of the skill
    '''
    ally = input()
    match ally:
        case "1": return member.skill(warrior)
        case "2": return member.skill(ranger)
        case "3": return member.skill(cleric)
        case "4": return member.skill(shaman)


def arena():
    '''
    Function that act as the "arena" for the Characters.
    The Player and Monster will take action for each turn.
    '''

    #Define the heroes's name
    warrior_name = input('Insert your name: ')
    ranger_name = "Condoriano"
    cleric_name = "Patricia"
    shaman_name = "Samsudin"
    monster_name = "Digital Lord"

    #Take input from user to select monster's difficulty
    difficulty = input("Choose your difficulty :\n1. Easy\n2. Normal\n3. Hard\n4. YOUR WORST NIGHTMARE!!!! \n Your choice: ")

    while (True):
        #Declaring All Hero classes into variables
        warrior = Warrior(warrior_name,100,80,20)
        ranger = Ranger(ranger_name,80,60,15)
        cleric = Cleric(cleric_name,120,60,10)
        shaman = Shaman(shaman_name,70,80,10)

        #Make a list of Heroes
        team = [warrior,ranger,cleric,shaman]
        
        match difficulty: #matching the user's input to available difficulty.
            case "1": monster = Monster(monster_name,200,70,25) 
            case "2": monster = Monster(monster_name,350,70,30) 
            case "3": monster = Monster(monster_name,475,70,35) 
            case "4": monster = Monster(monster_name,600,70,40)
        
      
        while monster.is_alive() and any(member.is_alive() for member in team):
            #Player's turn
            for member in team:
                if member.is_alive():
                    if member.curr_base_atk != member.base_atk:
                        member.update_effect()
                    stat(team, monster)
                    time.sleep(1)
                    team_action(team,member,warrior,ranger,cleric,shaman,monster)
                   
                if not monster.is_alive():
                    break

                time.sleep(1)

            #Monster's turn
            if monster.is_alive():
                if monster.curr_base_atk != monster.base_atk:
                    monster.update_effect()
                stat(team, monster)
                time.sleep(1)
                print(f"\n{monster.name}'s turn")
                available_target = [member for member in team if member.is_alive()] 
                monster_action(monster,available_target)
                time.sleep(1)
                
        #Winner Announcement
        print("=============================")
        if monster.is_alive():
            print(f'{monster.name} win')
            revive = input('You want to have a rematch? (y/n) : ')
            if revive.lower() == 'y':
                print('rematch begin')
                time.sleep(3)
            else:
                print('Game Over!')
                time.sleep(3)
                break
        else:
            print(f"Congratulations! You defeated The {monster.name}!")
            time.sleep(3)
            break
        print("=============================")

   
    
    



