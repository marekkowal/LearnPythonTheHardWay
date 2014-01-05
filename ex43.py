__author__ = 'marek'
from sys import exit

class Scene(object):

    def enter(self):
        print "You've just entered a scene! But you should not be really" \
              " seeing this message. This is the master class's method. " \
              "Implement the right one in the actual subclass."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        print "Starting the game engine."
        self.scene_map = scene_map
        print "I was initiated with ", scene_map, " as the starting scene."

    def play(self):
        print "Ok, let's play. First, I will open the scene, and then go into " \
              "an endless loop (here), playing subsequent scenes."
        current_scene = self.scene_map.opening_scene()
        print "The first scene to play is", current_scene

        while True:
            print "\n----------"
            next_scene_name = current_scene.enter()
            print "Next scene:", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "I am given the next scene:", current_scene


class Death(Scene):

    def enter(self):
        print "Ouch, you die! Game over!"
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "Hi, welcome to central corridor!"
        print "There's a pill lying on the floor, and there is a door too."
        print "What do you do? take the pill or open the door?"
        answer = raw_input("> ")
        if answer == "take the pill":
            print "Ok. Taking the pill"
            return "death"
        elif answer == "open the door":
            print "Ok. Opening the door."
            return "the bridge"
        else:
            print "What???"
            return "death"


class LaserWeaponArmory(Scene):

    def enter(self):
        print "Welcome to Laser Weapon Armory. The room is empty. There's only" \
              "a door behind you. Which door to open?"
        answer = raw_input("> ")
        if answer == "behind":
            return "the bridge"
        else:
            return "death"


class TheBridge(Scene):

    def enter(self):
        print "Welcome to the bridge. There's a monster here, asking you a" \
              "question. But there is also a door at the left, right, and" \
              " behind you. Which one do you open?"
        answer = raw_input("> ")
        if answer == "left":
            return "laser weapon armory"
        elif answer == "right":
            return "escape pod"
        elif answer == "behind":
            return "central corridor"
        else:
            return "death"


class EscapePod(Scene):

    def enter(self):
        print "Congratulations! You have reached the escape pod. Now, enter" \
              " the password to safely escape!"
        exit(1)


class Map(object):

    scenes = {"central corridor": CentralCorridor(),
              "the bridge": TheBridge(),
              "death": Death(),
              "laser weapon armory": LaserWeaponArmory(),
              "escape pod": EscapePod()}

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "Start_scene in __init__:", start_scene

    def next_scene(self, scene_name):
        print "Serving the object of Next scene"
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()