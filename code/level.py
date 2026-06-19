#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))


    def run(self, ):
        pass
