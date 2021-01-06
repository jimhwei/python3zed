"""
Notes:
room - two rooms
map - from one room to another room
player - (engine?)
victory
failure
"""

from sys import exit

"""
#demonstration of what a class scene would look like:

class Scene(object):
    
    def enter(self):
        pass"""

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
            current_scene.enter()

class Death(Scene):
    
    lines = [
                "You crashed into a blackhole, stretching into nothingness",
                "You died from snoo snoo"
                ]
    
    def enter(self):
        print(Death.quips[randint, len(self.lines)-1])
        exit(1)

class Zap_Ship(Scene):
    
    def enter(self):
        print("""
              You find yourself on Captain Zapp Brannigan's ship
              with no other crew onboard. You are the only pilot who 
              can fly the ship. To your left is an uncharted planet
              and to your right is a blackhole.""")
        
        action = input("> ")
        
        if action == "go left":
            print("""The ship responded to your steering and dashed
                         right into the strange planet
                         """)
            return 'amazon'
        
        if action == "go right":
            print("""You plunge straight into the void.
                  """)
            
            return 'death'
        
        else:
            print("Try again")
            return 'zap_ship'
    
class Amazon(Scene):
    
    def enter(self):
        pass
    
class Victory(Scene):
    
    def enter(self):
        pass

class Map(object):
    
    scenes = {
            'death': Death(),
            'zap_ship': Zap_Ship(),
        }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        pass


a_map = Map('zap_ship')
a_game = Engine(a_map)
a_game.play()