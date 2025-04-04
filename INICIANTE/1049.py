from collections import namedtuple

Animal = namedtuple('Animal', ['spine', 'origin', 'diet', 'name'])

animals = {
    Animal('vertebrado', 'ave', 'carnivoro', 'aguia'),
    Animal('vertebrado', 'ave', 'onivoro', 'pomba'),
    Animal('vertebrado', 'mamifero', 'onivoro', 'homem'),
    Animal('vertebrado', 'mamifero', 'herbivoro', 'vaca'),
    Animal('invertebrado', 'inseto', 'hematofago', 'pulga'),
    Animal('invertebrado', 'inseto', 'herbivoro', 'lagarta'),
    Animal('invertebrado', 'anelideo', 'hematofago', 'sanguessuga'),
    Animal('invertebrado', 'anelideo', 'onivoro', 'minhoca'),
}
resp = []
for i in range(3):
    resp.append(input())

choice = (resp[0], resp[1], resp[2])
    
for i in animals:
    if (i.spine, i.origin, i.diet) == tuple(choice):
        print(i.name)
        break 