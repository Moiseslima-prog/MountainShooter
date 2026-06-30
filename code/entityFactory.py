#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', position= (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', position=(10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', position=(WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))
            case 'Enemy2':
                return Enemy('Enemy2', position=(WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))
