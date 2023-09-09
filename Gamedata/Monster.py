'''
Module to define the Monster class, one of the Character's child class
'''
import random
import time
from .Character import *

class Monster(Character):

    def normal_atk(self,target1,target2):
        '''
        Normal attack of the monster. Attack two random heroes.
        The damage is between current base attack and a half of it.
        The heroes can take different damage
        '''
        damage1 = random.randint(int(self.curr_base_atk/2), self.curr_base_atk)
        print(f"{self.name} did a normal attack to {target1.name}")
        damage2 = random.randint(int(self.curr_base_atk/2), self.curr_base_atk)
        print(f"{self.name} did a normal attack to {target2.name}")
        time.sleep(1)
        target1.dmg_taken(damage1)
        target2.dmg_taken(damage2)
        self.energy_regen()

    def skill(self,target1,target2,target3,target4):
        '''
        Skill of the monster. Do the four times attacks. Each target is random between all heroes.
        The damage is between current base attack and a half of it times 0.5. 
        '''
        self.energy -= 20
        print(f"{self.name} is using skill")
        time.sleep(1)
        damage = int(random.randint(int(self.curr_base_atk/2), self.curr_base_atk) * 0.5)
        target1.dmg_taken(damage)
        target2.dmg_taken(damage)
        target3.dmg_taken(damage)
        target4.dmg_taken(damage)
        self.energy_regen()

    def ultimate(self, target):
        '''
        Ultimate skill of the monster. Attack all heroes.
        The damage is twice of the current base attack.
        '''
        self.energy = 0
        damage = self.curr_base_atk * 2
        target.dmg_taken(damage)
        
    def heal(self):
        '''
        Monster's self healing. heal HP by a quarter of monster's maximum HP
        '''
        self.energy -= 20
        self.hp += int(0.25 * self.max_hp)
        self.hp_limit()
        print(f"{self.name}'s HP has been healed by {int(0.25 * self.max_hp)}")
        time.sleep(1)
    
    

