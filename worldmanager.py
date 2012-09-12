""" World manager for alife sim

I K Stead, 11-09-2012

This will contain a class that stores all the global data for the world,
including a list of entities, manages creation and deletion of entities, 
and calls the subsystems in the main loop.
"""
import pygame
import entitytypes
import movement

class World(object):
    """Represent and manage the 'world' of the sim."""
    def __init__(self, size_x, size_y, entities=None, systems=None, max_e=1000):
        self.x = size_x
        self.y = size_y
        self.max_entities = max_e
        self.entities = []
        self.systems = []

        self.display_init()

    def new_entity(self, entity_type, fname, pos="random"):
        """Add a new entity of selected type to world entity list"""
        if len(self.entities) < self.max_entities:
            new = getattr(entitytypes, entity_type)
            # Randomise initial position if required
            if pos == "random":
                new["position"] = movement.random_pos(self.x, self.y)
            self.entities.append(new)
        else:
            raise Exception("Max number of entities exceeded")

    def display_init(self):
        """Set up the Pygame parts of the world object, and the control vars"""
        # Pygame setup
        pygame.__init__("world")
        self.exit = False
        self.display = pygame.display.set_mode((self.x*10, self.y*10))
        pygame.display.set_caption("Alife program")
        self.clock = pygame.time.Clock()

    def render(self):
        """Draw all entities to screen"""
        for entity in self.entities:
            if "position" in entity:
                # Add padding depending on display/grid size, hardcoded atm
                pos = map(lambda x: x*10, entity["position"])
                pygame.draw.circle(self.display, entity["colour"], pos, 1)

    def update(self):
        """Call systems on entity list and update display"""
        for system in self.systems:
            system.update(self.entities)
        self.render()
        self.clock.tick(20)
        pygame.display.flip()
