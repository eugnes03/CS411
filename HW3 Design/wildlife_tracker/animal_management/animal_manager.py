from typing import Optional, Dict
from animal import Animal

class AnimalManager:
    #Section 1
    def __init__(self) -> None:
        self.animals: Dict[int, Animal] = {}
    def register_animal(self, animal: Animal) -> None:
        pass

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass

