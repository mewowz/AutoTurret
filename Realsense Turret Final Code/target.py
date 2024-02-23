from polyreg import Point, Points

class Target:
    """
    A struct-like object that stores Points with a reference
    to a specific target. It's a way to give a set of points something
    distinct about them.
    """

    def __init__(self, uid, pos=None, max_pos=None):
        if type(pos) == Points:
            self.pos = pos
        elif type(pos) == Point:
            self.pos = Points([pos])
        else:
            self.pos = Points()

        self.max_pos = max_pos
        self.uid = uid
    


class Targets:
    """
    Just a container with some helper functions for handling a set
    of targets
    """
    def __init__(self, targets=None):
        self.targets = {}
        if targets == None:
            return
        for t in targets:
            self.targets[t.uid] = t


    def add(self, target):
        if tar.uid not in self.targets.keys():
            self.targets[tar.uid] = target
        else:
            return False
    
    def remove(self, uid):
        if uid in self.targets.keys():
            del self.targets[uid]



        

