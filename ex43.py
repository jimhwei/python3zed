from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("need to be reconfigured, currently a place holder")
        exit(1)


#this is where it gets tricky...
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = ["You died, Haha.",
                 "Try harder next time!",
                 "Stay determined"]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        # from death make quips choose randint from 0 to length
        # of self.quip - 1, this way the list can go on
        exit(0)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              The Gothons of Planet Percal #25 have invaded your ship and
              destroyed your entire crew. You are the last surviving member
              and your last mission is to get the neutron destruct bomb from
              the Weapons Armory, put it in the bridge, and blow the ship
              up after getting into an escape pod. You're running down the
              central corridor to the Weapons Armory when a Gothon jumps out,
              red scaly skin, dark grimy teeth, and evil clown costume flowing
              around his hate filled body. He's blocking the door to the
              Armory and about to pull a weapon to blast you.
              You can "shoot", "dodge", "tell a joke"
              """))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon. His clown costume is flowing and moving
                  around his body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This completely ruins his brand new costume his mother
                  bought him, which makes him fly into an insane rage
                  and blast you repeatedly in the face until you are dead.
                  Then he eats you. """))
            return 'death'

        elif action == "dodge":
            print(dedent("""
                  Like a world class boxer you dodge, weave, slip and
                  slide right as the Gothon's blaster cranks a laser
                  past your head. In the middle of your artful dodge
                  your foot slips and you bang your head on the metal
                  wall and pass out. You wake up shortly after only to
                  die as the Gothon stomps on your head and eats you.
                  """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                  Lucky for you they made you learn Gothon insults in the
                  academy. You tell them the one Gothon joke you know:
                  blerga blerga turga, herga turka. The Gothon stops,
                  tries not to laugh, then busts out laughing. You shoot him in
                  in the face and jump through the Weapon Armory door."""))
            return 'laser_weapon_armory'

        else:
            print("Does not compute!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              You do a dive roll into the Weapon Armory. The code is 3 digits.
              """))

#        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        code = "123"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 2:
            print("BZZZEDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                    The container clicks open and the seal breaks, letting
                    gas out. You grab the bomb and put it in the right spot.
                    """))
            return 'the_bridge'

        else:
            print(dedent("""
                    The lock buzzes one last time and then you hear a sound.
                    Gothons blow up the ship and YOU DIE.
                    """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              You burst onto the Bridge with the bomb. They don't shoot you
              because they see you have a bomb.
              You can "throw the bomb" or "slowly place the bomb"
              """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                  In a panic you throw the bomb and jump for the door.
                  The bomb blows up and everyone dies
                  """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                  You point your blaster at the bomb and the Gothons get scared.
                  You place the bomb and get to the escape pod.
                  """))

            return 'escape_pod'
        else:
            print("Does not compute!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
              You rush through the ship trying to get out
              before the ship blows. There are five pods, which one 
              do you take? Enter a number from 1-5.
              """))

        #good_pod = randint(1,5)
        good_pod = 3
        guess = input ("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                  You jump into pod {guess} and hit eject.
                  The windshield had a crack and it blows up.
                  """))
            return 'death'

        else:
            print(dedent(f"""
                  You jump into pod {guess} and hit the eject button.
                  The enemy ship blows up. You win!
                  """))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    #this is a dictionary, this is is used to key in returns from each scene
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        #get scene_names from map.scenes
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


"""FSM, a model of computation based on a 
hypothetical machine made of one or more states.
Only one state can be active at a time. 
Used to organize an execution flow for
doing things one step at a time.
e.g. cards and nodes, where the cards are an action
cannot have more than one node at a time"""