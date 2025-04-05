from gameplay import *
from gameplay.devices.keyboard import f, release_keys, wf

class CombatAgent:

    def __init__(self, toggle_combat_thread):
        self.toggle_combat_thread = toggle_combat_thread
        pass
    
    def start_combat(self):
        far_tolerance = 600
        center_of_screen_x = 960
        center_of_screen_y = 570
        while True:
            if self.toggle_combat_thread.is_set():
                print('🔴 Combat')

                star_is_visible, star_position = locate_star_from_screenshot()
                center_to_star_x_distance = abs(star_position[0] - center_of_screen_x)
                center_to_star_y_distance = abs(star_position[1] - center_of_screen_y)

                if (abs(center_to_star_x_distance) > far_tolerance or abs(center_to_star_y_distance) > far_tolerance):
                    wf()
                    print('walk and interact')
                else:
                    f()
                    print('interact')

            else:
                self.toggle_combat_thread.wait()
            time.sleep(1)