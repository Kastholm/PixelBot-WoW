from gameplay import *
from gameplay.devices.keyboard import w, we, wf, wq, wspace, wz, z

class MovementAgent:

    def __init__(self, toggle_movement_thread, queued_enemy_indicator):
        self.toggle_movement_thread = toggle_movement_thread
        self.queued_enemy_indicator = queued_enemy_indicator
        self.enemyIndicator = False

    def walk_jump(self):
        wspace()
    
    def target_scan_interact(self, enemyIndicator):
        if enemyIndicator == 'YELLOW' or enemyIndicator == 'RED':
            wf()
        else:
            wz()
        w()
        print('click')
    
    def strafe_jump(self, enemyIndicator):
        for _ in range(2):
            if self.toggle_movement_thread.is_set():
                self.target_scan_interact(self, enemyIndicator)
                w()
                wq()
                we()
                print('click')
    
    def start_movement(self):
        roll_dice = random.randint(1,4)
        while True:
            if self.toggle_movement_thread.is_set():
                print('🟢 Movement')
                self.enemyIndicator = get_latest(self.queued_enemy_indicator)

                if roll_dice in [1,2,3]:
                    self.target_scan_interact(self.enemyIndicator)
                else:
                    self.strafe_jump(self.enemyIndicator)

            else:
                self.toggle_movement_thread.wait()
            time.sleep(0.1)