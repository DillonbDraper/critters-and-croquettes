class Iguana:
    
    def __init__(self, id, name, date_added, species ="iguana"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Bullfrog:
    
    def __init__(self, id, name, date_added, species ="bullfrog"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True
    
    def __str__(self):
        return f"{self.name} is a {self.species}"

class Python:
    
    def __init__(self, id, name, date_added, species ="python"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Gardner:
    
    def __init__(self, id, name, date_added, species ="gardner"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Komodo:
    
    def __init__(self, id, name, date_added, species ="Komodo"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"