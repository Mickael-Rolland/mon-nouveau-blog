import json
from .models import Animal, Equipement


def create():
    delete()
    équipement_data = 'blog/équipement.json'
    with open(équipement_data, "r") as f:
        équipement_dict = json.load(f)
        for id_équip in équipement_dict:
            disponibilité = équipement_dict[id_équip]["DISPONIBILITÉ"]
            Equipement.objects.create(id_equip=id_équip, disponibilite=disponibilité)

    animal_data = 'blog/animal.json'
    with open(animal_data, "r") as f:
        animal_dict = json.load(f)
        for id_animal in animal_dict:
            état = animal_dict[id_animal]["ETAT"]
            type = animal_dict[id_animal]["TYPE"]
            race = animal_dict[id_animal]["RACE"]
            lieu = animal_dict[id_animal]["LIEU"]
            photo = animal_dict[id_animal]["PHOTO"]
            Animal.objects.create(id_animal=id_animal,
                                  etat=état,
                                  type=type,
                                  race=race,
                                  lieu=Equipement.objects.get(id_equip=lieu),
                                  photo=photo)


def delete():
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()

    for animal in animaux:
        animal.delete()
    for equipement in equipements:
        equipement.delete()
