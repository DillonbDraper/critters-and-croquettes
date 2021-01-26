class Llama:

    def __init__(self, id, name, date_added, shift, species ="llama"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Horse:
    
    def __init__(self, id, name, date_added, shift, species ="horse"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Goat:
    
    def __init__(self, id, name, date_added, shift, species ="goat"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Pony:
    
    def __init__(self, id, name, date_added, shift, species ="pony"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Ferret:
    
    def __init__(self, id, name, date_added, shift, species ="ferret"):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date_added
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"