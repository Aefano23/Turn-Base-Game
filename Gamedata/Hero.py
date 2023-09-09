'''
Module to define the heroes class. All of them are child class of Character
'''
import random
import time
from .Character import *

class Warrior (Character):
    '''
    Warrior class. Focus on dealing damage to the Monster
    '''
    def skill(self,target):
        '''
        Warrior's Skill. Single target attack
        The damage is between current base attack and a half of it times 2
        '''
        self.energy -= 20
        damage = random.randint(int(self.curr_base_atk/2), self.curr_base_atk) * 2
        print(f"{self.name} is using skill to {target.name}")
        time.sleep(1)
        target.dmg_taken(damage)
        self.energy_regen()

    def ultimate(self, target):
        '''
        Warrior's Ultimate. Single Target Attack
        Consume Half of the warrior's current HP.
        The damage is current base attack plus HP loss.
        '''
        self.energy = 0
        damage = self.curr_base_atk + int(0.5*self.hp)
        self.hp -= int(0.5*self.hp)
        print(f"{self.name}'s HP has been consumed by half")
        time.sleep(1)
        print(f"{self.name} using ultimate skill to {target.name}")
        time.sleep(1)
        target.dmg_taken(damage)
        self.energy_regen()
        
class Ranger (Character):
    '''
    Ranger class. Can reduce enemy's attack and deal decent damage
    '''
    def skill(self,target):
        '''
        Ranger's Skill. Reduce enemy's attack by half.
        The effect lasts for 2 turns
        '''
        self.energy -= 20
        print(f"{self.name} is using skill to {target.name}")
        time.sleep(1)
        atk_debuff = 0.5
        duration = 3
        target.atk_change(atk_debuff,duration)
        print(f"{target.name}'s attack has been reduced by half")
        time.sleep(1)
        
    def ultimate(self, target):
        '''
        Ranger's Ultimate. Single Target Attack
        The damage is between current base attack and a half of it times 3
        '''
        self.energy = 0
        damage = random.randint(int(self.curr_base_atk/2), self.curr_base_atk) * 3
        print(f"{self.name} using ultimate skill to {target.name}")
        time.sleep(1)
        target.dmg_taken(damage)
        self.energy_regen()

class Cleric (Character):
    '''
    Cleric class. Provides healing to the allies
    '''
    def skill(self,target):
        '''
        Cleric's Skill. Restore an ally's HP by 0.25 of cleric's maximum HP
        '''
        self.energy -= 20
        print(f"{self.name} is using skill to {target.name}")
        time.sleep(1)
        target.hp += int(0.25 * self.max_hp)
        target.hp_limit()
        print(f"{target.name}'s HP has been healed by {int(0.25 * self.max_hp)}")
        time.sleep(1)
        
    def ultimate(self, target):
        '''
        Cleric's Ultimate. Restore all allies's HP by 0.5 of cleric's maximum HP
        '''
        self.energy = 0
        target.hp += int(0.5 * self.max_hp)
        target.hp_limit()

class Shaman (Character):
    '''
    Shaman class. Can buff attack and recharge energy of an ally
    '''
    def skill(self,target):
        '''
        Shaman's skill. Double an ally's attack
        '''
        self.energy -= 20
        print(f"{self.name} is using skill to {target.name}")
        time.sleep(1)
        atk_buff = 2
        duration = 3
        target.atk_change(atk_buff,duration)
        print(f"{target.name}'s attack has been double")
        time.sleep(1)
        
    def ultimate(self,target):
        '''
        Shaman's Ultimate. Recharge an ally's energy
        '''
        self.energy = 0
        print(f"{self.name} is using ultimate skill to {target.name}")
        time.sleep(1)
        target.energy += int(0.5*target.max_energy)
        target.energy_limit()
        print(f"{target.name}'s energy has been recharged by {int(0.5*target.max_energy)}")
        time.sleep(1)
        

