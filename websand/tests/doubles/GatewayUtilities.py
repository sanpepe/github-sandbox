import copy
import uuid

from websand.src.Entity import Entity

class GatewayUtilities(Entity):
    def __init__(self):
        self.entities = dict()
        #print("GatewayUtilities __init__ {}".format(self.__class__))

    def getEntities(self):
        clonedEntities = list(self.entities.values())
        return clonedEntities

    def save(self, entity):
        if entity.getID() is None:
            entity.setID(str(uuid.uuid4()))
        ID = entity.getID()
        self.entities[ID] = copy.deepcopy(entity)
        return entity

    def delete(self, entity):
        self.entities.pop(entity.getID())


