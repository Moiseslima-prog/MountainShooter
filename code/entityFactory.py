#!/usr/bin/python
# -*- coding: utf-8 -*-

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range (7):
                    list_bg.append(Background(f'Level1Bg{1}'))
                return list_bg