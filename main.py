class Person:
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.partner = None
        self.children = []    
    
    def add_partner(self, partner):
        if self.partner is not None:
            print(f"{self.name} ya tiene una pareja: {self.partner.name}.")
        else:
            self.partner = partner
            partner.partner = self
            print(f"{self.name} es pareja de {partner.name}.")
    
    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            print(f"{self.name} ha tenido un hijo: {child.name}")
        else: 
            print(f"{child.name} ya es un hijo de {self.name}")