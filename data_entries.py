class dataEntry():
    def __init__(self, name, variants = None):
        self.name = name
        self.variants = variants

class foreignKey():
    def __init__(self, name, correspondingClass):
        self.name = name
        self.foreignClass = correspondingClass

    @property
    def Class(self):
        return self.foreignClass

    @property
    def ClassName(self):
        return self.foreignClass.__name__

    @property
    def ClassTable(self):
        return self.foreignClass.table_name