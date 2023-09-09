'''
Module to define the Character class, which is a parent class of Hero and Monster
'''
import random
import time

class Character():
    def __init__(self, name, hp, energy, base_atk):
        '''
        Define the character's attribute
        '''
        self.name = name # character's name
        self.max_hp = hp # character's maximum HP
        self.hp = hp # character's current HP
        self.max_energy = energy # character's maximum Energy
        self.energy = 0 # character's current energy
        self.base_atk = base_atk # character's base attack
        self.curr_base_atk = base_atk # character's current base attack
        self.effect_duration = 0 # character's effect's (buff/debuff) duration left

    def is_alive(self):
        '''
        Return value that make the character is alive
        '''
        return self.hp > 0
    
    def normal_atk(self,target):
        '''
        character's normal attack. Single target attack.
        The damage is between current base attack and a half of it.
        '''
        damage = random.randint(int(self.curr_base_atk/2), self.curr_base_atk)
        print(f"{self.name} did a normal attack to {target.name}")
        self.energy_limit()
        time.sleep(1)
        target.dmg_taken(damage)
        self.energy_regen()

    def energy_regen(self):
        '''
        character's energy regeneration
        '''
        if self.energy < self.max_energy:
            self.energy += 10
    
    def energy_limit(self):
        '''
        Maintain the energy to not exceed the maximum value
        '''
        if self.energy > self.max_energy:
            self.energy = self.max_energy
            print(f'{self.name} energy has fully recharged')
        elif self.energy < 0:
            self.energy = 0
            
    def hp_limit(self):
        '''
        Maintain the HP to not exceed the maximum value
        '''
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            print(f'{self.name} HP has fully restored')

    def dmg_taken(self, damage):
        '''
        Applying damage to the character
        '''
        self.hp -= damage
        self.energy_regen()
        self.energy_limit()
        print(f"{self.name} take {damage} damage")
        time.sleep(1)

    def atk_change(self,multiplier,duration):
        '''
        change the base attack damage value due to buff/debuff
        '''
        self.curr_base_atk = int(self.base_atk * multiplier)
        self.effect_duration = duration

    def update_effect(self):
        '''
        update the buff/debuff duration
        '''
        if self.effect_duration > 0:
            self.effect_duration -= 1
            print(f"{self.name} effect turn left : {self.effect_duration} \n")
            if self.effect_duration == 0:
                self.curr_base_atk = self.base_atk
                print(f"{self.name} effect has been dispelled \n")


    



   

    
        
    


            
    

    
        
        
        
    

