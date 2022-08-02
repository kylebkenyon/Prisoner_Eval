import random
import math
from Box import Box

class BoxRoom:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes
        self.num_to_check = math.floor(self.num_boxes/2)
        self.Boxes = []
        
        for i in range(self.num_boxes):
            self.Boxes.append(Box(i))
            
        random.shuffle(self.Boxes)
        
    def print_list(self):
        for i in range(self.num_boxes):
            print(self.Boxes[i].number)
            
    def exploreBoxRoom(self, p) -> bool:
        check_box = p
        for i in range(self.num_to_check):
            if self.Boxes[check_box].number == p:
                return True
            check_box = self.Boxes[check_box].number
            
        return False
