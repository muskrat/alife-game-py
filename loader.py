"""
Load creature definitions from YAML to Python dicts

I K Stead, 13-09-2012
"""
import yaml

class Loader(object):
    """Opens/Closes YAML files and parses them to yield creature dicts"""
    def __init__(self, fname):
        self.yaml = self.load(fname)

    def load(self, fname):
        """Open YAML, parse it and save the result, then close it"""
        try:
            f = open(fname, 'r')
            y = yaml.load(f)
            f.close()
        except IOError as error:
            print error
            y = None
        return y

    def new_entity(self, name):
        """Return a new entity dict from parsed YAML"""
        try:
            # `copy`, otherwise will return a reference to self.yaml
            return self.yaml[name].copy()
        except KeyError as error:
            print error
            return None


