from gameplay import *
from gameplay.combat.main import CombatAgent
from gameplay.movement.main import MovementAgent
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


        self.movement_agent = MovementAgent(self.toggle_movement_thread)
        self.combat_agent = CombatAgent(self.toggle_combat_thread)

        self.threads = {
            'movement': threading.Thread(target=self.movement_agent.start_movement),
            'combat': threading.Thread(target=self.combat_agent.start_combat),
        }

    def start_bot(self):
        while True:
            if self.toggle_bot_thread.is_set():
                print('Play!')
                
                #Load Route And Allowed Coordinates
                #Start Moving & Combat

                #Movement.py indtil target er tæt på?
                #Når target tæt på med event stop Movement og start combat
                #Når target død eller ingen stjerne event stop Movement og start combat

                time.sleep(5)
            else:
                self.toggle_movement_thread.clear()
                self.toggle_combat_thread.clear()
                self.toggle_bot_thread.wait()

        

        """                 Dette er en combat bot.

        TLDR - Kan gå indenfor visse koordinater og kæmpe mod mobs.

        Det første man vælger er hvilken route man vil benytte.
        fx 1-6 Dun Morogh.

        Så ved den hvilke coordinates den må holde sig inden for.

        Mens den går SCANNER den efter targets.


        That's it. Dont over complicate it """