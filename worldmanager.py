""" World manager for alife sim

I K Stead, 11-09-2012

This will contain a class that stores all the global data for the world,
including a list of entities, manages creation and deletion of entities, 
and calls the subsystems in the main loop.
"""
import pygame
import colours
import movement
import threading
import loader

class World(object):
    """Represent and manage the 'world' of the sim."""
    def __init__(self, size_x, size_y, yaml, max_e=1000, fps=20):
        self.x = size_x
        self.y = size_y
        self.max_entities = max_e
        self.entities = []
        self.fps = fps
        self.loader = loader.Loader(yaml)

    def add_entity(self, e_type, pos="random"):
        """Add a new entity of selected type to world entity list"""

        if len(self.entities) < self.max_entities:
            new = self.loader.new_entity(e_type)
            # Randomise initial position if required
            if pos == "random" and new is not None:
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
                pygame.draw.circle(self.display, entity["colour"], pos, 10)

    def update(self):
        """Call systems on entity list and update display"""
        # Debugging
        movement.update(self.entities)

        self.display.fill(colours.black)
        self.render()
        self.clock.tick(self.fps)
        pygame.display.flip()

    def run(self):
        """Main loop. Run update method in a loop and scan for input.
        
        We run this method inside a thread so user can change world params
        while the sim is running."""
        def worker():
            self.display_init()
            while not self.exit:
                # Check for user input; move this into separate method later
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.exit = True # Leave main loop
                for key in pygame.key.get_pressed():
                    if key == pygame.K_ESCAPE:
                        self.exit = True
                self.update()
            # Destroy pygame window
            pygame.display.quit()
        
        # Instantiate a thread targeting `worker` and start it
        run_thread = threading.Thread(target=worker)
        run_thread.start()


def main():
    """Allows running of this file for testing"""
    w = World(100, 100, "creatures.yaml")
    for i in xrange(3):
        w.add_entity("amoeba")
    w.run()

if __name__ == "__main__":
    main()
