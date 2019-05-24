import sys

sys.path.append('/home/nbuser/library/')
# This is used to include files which are in the same folder.

from utils import *
from agents import *
from KeepTrackOfAllMyThings import *
# agents.py must be in the same folder as the notebook
# utils.py must be in the same folder as the notebook


class GraphicRoom(GraphicEnvironment):
    def __init__(self, width=10, height=10, boundary=True, color={}, display=False):
        super().__init__(width, height, boundary, color, display)

    def thing_classes(self):
        return [Wall, Dirt, Bump, ReflexVacuumAgent, RandomVacuumAgent,
                TableDrivenVacuumAgent, ModelBasedVacuumAgent]

    def percept(self, agent):
        '''return a list of things that are in our agent's location'''
        things = self.list_things_at(agent.location)
        return things

    def execute_action(self, agent, action):
        '''changes the state of the environment based on what the agent does.'''
        # This bump was from the last move, so remove it
        items = self.list_things_at(agent.location, tclass=Bump)
        if len(items) != 0:
            self.delete_thing(items[0])

        if action == 'turnright': # Based on the direction the vacuum is moving, turning right for it is turning left for us, i think.
            print('{} decided to {} at location: {}'.format(str(agent)[1:-1], action, agent.location))
            if agent.direction.direction == Direction('down').direction:
                agent.direction = Direction('left')
            elif agent.direction.direction == Direction('left').direction:
                agent.direction = Direction('up')
            elif agent.direction.direction == Direction('up').direction:
                agent.direction = Direction('right')
            elif agent.direction.direction == Direction('right').direction:
                agent.direction = Direction('down')

        elif action == 'turnleft':
            print('{} decided to {} at location: {}'.format(str(agent)[1:-1], action, agent.location))
            if agent.direction.direction == Direction('down').direction:
                agent.direction = Direction('right')
            elif agent.direction.direction == Direction('right').direction:
                agent.direction = Direction('up')
            elif agent.direction.direction == Direction('up').direction:
                agent.direction = Direction('left')
            elif agent.direction.direction == Direction('left').direction:
                agent.direction = Direction('down')
        elif action == 'moveforward':
            loc = copy.deepcopy(agent.location)  # find out the target location
            if agent.direction.direction == 'right':
                loc[0] += 1
            elif agent.direction.direction == 'left':
                loc[0] -= 1
            elif agent.direction.direction == 'down':
                loc[1] += 1
            elif agent.direction.direction == 'up':
                loc[1] -= 1
            if self.is_inbounds(loc):  # move only if the target is a valid location
                print('{} decided to move {}wards at location: {}'.format(str(agent)[1:-1], agent.direction.direction,
                                                                          agent.location))
                agent.moveforward()
                agent.location = loc  # We can move forward so update it...the vacuum doesn't know anything
            else:
                print('{} decided to move {}wards at location: {}, but couldn\'t'.format(str(agent)[1:-1],
                                                                                         agent.direction.direction,
                                                                                         agent.location))
                self.add_thing(Bump(), agent.location)
                print(self.list_things_at(agent.location))
                agent.moveforward(False)

        elif action == "clean":
            items = self.list_things_at(agent.location, tclass=Dirt)
            if len(items) != 0:
                print('{} cleaned {} at location: {}'
                      .format(str(agent)[1:-1], str(items[0])[1:-1], agent.location))
                self.delete_thing(items[0])

    def is_done(self):

        return False


class Dirt(Thing):
    pass


class Bump(Thing):
    pass


class Vacuum(Agent):
    randomdirection = ["up", "down", "left", "right"]   #picks a direction at random
    direction = Direction(random.choice(randomdirection))

    def clean(self, thing):
        print("Vacuum Cleaned Location {}.".format(self.location))

    def moveforward(self, success=True):
        if not success:
            print('\n *bump*')
            print('oof ouch owie :(')
            print('walls hurt\n')

        print("Vacuum Moved Forward {}.".format(self.location))


def program_simple(percepts):
    perceptsstring = ''.join(str(percepts))
    print('Percepts: {}'.format(perceptsstring))

    if 'Dirt' in perceptsstring:
        simple_stats.cleanedcountadd()
        return 'clean'
    if 'Bump' in perceptsstring:
        return 'turnleft'
    simple_stats.movedforwardcountadd()
    return 'moveforward'


def program_random(percepts):
    perceptsstring = ''.join(str(percepts))
    print('Percepts: {}'.format(perceptsstring))
    randoms = random.randrange(0, 100)

    if 'Dirt' in perceptsstring:
        random_stats.cleanedcountadd()
        return 'clean'

    if randoms < 10:        ### RANDOM ACTIONS
        return 'turnright'  ### 10% chance to turn right
    if randoms < 25:        ### 15% chance to turn left (has to be between 10 and 25)
        return 'turnleft'   ### 100% to be really cool

    if 'Bump' in perceptsstring:
        return 'turnleft'
    random_stats.movedforwardcountadd()
    return 'moveforward'


class VacuumTable:
    sensor = ['z', 'z', 'z', 'z']
    actions = ['a', 'a', 'a', 'a']

    def addsensor(self, newsensor):
        sensor = self.sensor
        for y in range(2, -1, -1):
            sensor[y+1] = sensor[y]
        sensor[0] = newsensor

    def addaction(self, newaction):
        actions = self.actions
        for y in range(2, -1, -1):
            actions[y+1] = actions[y]
        actions[0] = newaction

    def show(self):
        print("Sensor Inputs: {}".format(self.sensor))
        print("Actions Taken: {}".format(self.actions))

    def reset(self):
        self.sensor = ['z', 'z', 'z', 'z']
        self.actions = ['a', 'a', 'a', 'a']

    def analyze(self):
        actions = self.actions
        sensors = self.sensor

        if actions.count('Vacuum') > 2:
            print("\n\n Wow! I'm on a roll! :D\n\n")
        if actions.count('Forwards') == 4:   # if it moves forward 4 times in a row, it'll turn left or right
            turnaction = ['turnleft', 'turnright']
            choice = random.choice(turnaction)
            if choice == 'turnleft':
                self.addaction('Turn-Left')
            else:
                self.addaction('Turn-Right')
            return choice   # Turns left or right if it just moved forward 4 times

        if sensors.count('Dirty') > 2:       # if it just cleaned something twice, turn right
            if actions.count('Turn-Left') > 1:
                self.addaction('Turn-Right')
                return 'turnright'
            self.addaction('Turn-Left')
            return 'turnleft'

        return ''

remembertable = VacuumTable()


def program_remember(percepts):
    perceptsstring = ''.join(str(percepts))
    print('Percepts: {}'.format(perceptsstring))
    remembertable.show()

    if 'Dirt' in perceptsstring:
        remembertable.addsensor('Dirty')
        remembertable.addaction('Vacuum')
        table_stats.cleanedcountadd()
        return 'clean'

    takeaction = remembertable.analyze()    ##based on the table, decides what action should be taken.
    if takeaction is not '':
        return takeaction

    if 'Bump' in perceptsstring:
        remembertable.addsensor('Bump')
        remembertable.addaction('Turn-Left')
        return 'turnleft'

    remembertable.addsensor('Clean')
    remembertable.addaction('Forwards')
    table_stats.movedforwardcountadd()
    return 'moveforward'


