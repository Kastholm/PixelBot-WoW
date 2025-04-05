from gameplay import *
from gameplay.combat.main import CombatAgent
from gameplay.movement.main import MovementAgent
from gameplay.devices.keyboard import *
class BotAgent:

    def __init__(
                 self, toggle_bot_thread, queued_coordinates_indicator,
                 queued_combat_indicator, queued_enemy_indicator,
                 queued_health_indicator 
                 ):
        
        self.toggle_bot_thread = toggle_bot_thread
        self.toggle_movement_thread = threading.Event()
        self.toggle_combat_thread = threading.Event()

        self.queued_coordinates_indicator = queued_coordinates_indicator
        self.queued_combat_indicator = queued_combat_indicator
        self.queued_enemy_indicator = queued_enemy_indicator
        self.queued_health_indicator = queued_health_indicator

        self.inCombat = False
        self.enemyIndicator = None


        self.movement_agent = MovementAgent(self.toggle_movement_thread, self.queued_enemy_indicator)
        self.combat_agent = CombatAgent(self.toggle_combat_thread)

        self.threads = {
            'movement': threading.Thread(target=self.movement_agent.start_movement),
            'combat': threading.Thread(target=self.combat_agent.start_combat),
        }
    
    def start_threads(self):
        for thread in self.threads.values():
            thread.start()

    def start_bot(self):
        self.start_threads()
        no_enemy_counter = 0
        while True:
            if self.toggle_bot_thread.is_set():

                self.inCombat = get_latest(self.queued_combat_indicator)
                self.enemyIndicator = get_latest(self.queued_enemy_indicator)

                if self.inCombat == True:
                    no_enemy_counter = 0
                    self.toggle_movement_thread.clear()
                    self.toggle_combat_thread.set()
                #ELSE
                    #Inside Allowed Coordinates?
                        #IF NOT 
                            #Start movement bot, Relocate to coordinates
                            #self.toggle_movement_thread.set()

                elif self.enemyIndicator == 'YELLOW' or self.enemyIndicator == 'RED':
                    no_enemy_counter = 0
                    star_is_visible, star_position = locate_star_from_screenshot()
                    if star_is_visible == True:
                        self.toggle_movement_thread.clear()
                        self.toggle_combat_thread.set()
                    else:
                        self.toggle_combat_thread.clear()
                        self.toggle_movement_thread.set()
                
                elif no_enemy_counter >= 3:
                        self.toggle_combat_thread.clear()
                        self.toggle_movement_thread.set()

                else:
                    self.toggle_combat_thread.clear()
                    no_enemy_counter += 1
                    
            else:
                release_keys()
                self.toggle_movement_thread.clear()
                self.toggle_combat_thread.clear()
                self.toggle_bot_thread.wait()
            
            time.sleep(0.1)




                #Load Route

                #Checks
                #Already in combat?
                    #Start combat bot
                #ELSE
                    #Inside Allowed Coordinates?
                        #IF NOT 
                            #Start movement bot, Relocate to coordinates

                #Scan for a target with the target key
                    #IF enemy
                        #Interract with tar
                            #IF star is close
                                #Start combat

                    
                #Når target død eller ingen stjerne event stop Movement og start combat
        

        """                 Dette er en combat bot.

        TLDR - Kan gå indenfor visse koordinater og kæmpe mod mobs.

        Det første man vælger er hvilken route man vil benytte.
        fx 1-6 Dun Morogh.

        Så ved den hvilke coordinates den må holde sig inden for.

        Mens den går SCANNER den efter targets.


        That's it. Dont over complicate it """