""" Simple entity for alife program

I K Stead, 11-09-2012

An entity is just a dictionary that stores entity data in named
fields. Saving and loading will be done with JSON. Subsystems can select
entities from the world manager by filtering for entities with target 
fields.
"""
import colours

amoeba = {"name" : "Amoeba",
          "ID" : 0,
          "position" : None,
          "dest" : None,
          "colour" : colours.red
         }

plant = {"name" : "plant",
         "ID" : 0,
         "position" : None,
         "colour" : colours.green
        }
