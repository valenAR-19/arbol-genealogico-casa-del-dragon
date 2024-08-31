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
            print(f"{self.name} ha tenido un hijo: {child.name}.")
        else: 
            print(f"{child.name} ya es un hijo de {self.name}.")
            
class FamilyTree:
    
    def __init__(self):
        self.people = {}
        
    def add_person(self, id, name):
        if id in self.people:
            print(f"La persona con ID: {id} ya existe.")
        else:
            person = Person(id, name)
            self.people[id] = person
            print(f"La persona con nombre{name} [ID: {id}] ha sido añadida al arbol.")
    
    def remove_person(self, id):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f"La persona con nombre {person.name} [ID: {id} ha sido eliminada del arbol.]")
        else:
            print(f"La persona con ID: {id} no existe en el arbol.")
            
    def set_partner(self, id1, id2):
        if id1 in self.people and id2 in self.people:
            person1 = self.people[id1]
            person2 = self.people[id2]
            person1.add_partner(person2)
        else:
            print(f"Algun ID no existe en el arbol.")
            
    def add_child(self, parent_id, child_id):
        if parent_id in self.people and child_id in self.people:
            parent = self.people[parent_id]
            child = self.people[child_id]
            parent.add_child(child)
    
    def print_tree(self):
        pass