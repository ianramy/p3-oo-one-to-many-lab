class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        Pet.all.append(self)

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type}, owner={self.owner})"

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only instances of Pet can be added")
        if pet not in self._pets:
            pet.owner = self
            self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name={self.name})"

# Make sure to reset Pet.all between tests
def reset_pets():
    Pet.all = []
