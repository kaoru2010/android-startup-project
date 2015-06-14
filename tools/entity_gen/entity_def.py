class EntityBase(object):
    def __init__(self, name = None, ref = None, properties = None):
        self.name = name
        self.ref = ref
        self.properties = properties if properties is not None else []

class Entity(EntityBase):
    def accept(self, generator):
        if self.name is not None:
            generator.startEntity(self.name)
            for prop in self.properties:
                generator.addProperty(prop)
            generator.finishEntity()

        else:
            generator.reference(self.ref)

class ArrayProperty(EntityBase):
    def accept(self, generator):
        generator.addArray(self.name, self.ref)

class StringProperty(EntityBase):
    def accept(self, generator):
        generator.addString(self.name)

class IntegerProperty(EntityBase):
    def accept(self, generator):
        generator.addInteger(self.name)
