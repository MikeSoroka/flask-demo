class limitedVariantsDataEntry():
    def __init__(self, name, variants):
        self.name = name
        self.variants = variants

    def __str__(self):
        return self.name
class foreignKey():
    def __init__(self, name, correspondingClass):
        self.name = name
        self.foreignClass = correspondingClass

    def __eq__(self, other):
        return self.name == other.name and self.foreignClass == other.foreignClass

    def __key(self):
        return self.name, self.foreignClass

    def __hash__(self):
        return hash(self.__key())
    @property
    def Class(self):
        return self.foreignClass

    @property
    def ClassName(self):
        return self.foreignClass.__name__

    @property
    def ClassTable(self):
        return self.foreignClass.table_name

    def __str__(self):
        return self.name.lower()