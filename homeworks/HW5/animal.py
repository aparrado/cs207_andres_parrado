# -*- coding: utf-8 -*-
"""
Author: Andrés Parrado
"""



class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species

    @property
    def species(self):
        print("Getting value")
        return self._species
    
    @species.setter
    def species(self, into):
        print("Setting value")
        assert into in Animal.valid_species, Exception(f'invalid species: {into}')
        self._species = into
        

    def __repr__(self):
        return f'{self.name} ({self._species})'