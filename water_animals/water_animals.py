class Clownfish:
    
    def __init__(self, id, name, date_added, species ="clownfish"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Salmon:
    
    def __init__(self, id, name, date_added, species ="salmon"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Barracuda:
    
    def __init__(self, id, name, date_added, species ="barracuda"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Orca:
    
    def __init__(self, id, name, date_added, species ="orca"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Beluga:
    
    def __init__(self, id, name, date_added, species ="beluga"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

