from yaml import dumper
import cls_module as level
import yaml
import random

Levels = yaml.load(
'''
levels:
    - !easy_level {}
    - !medium_level
        enemy: ['rat']
    - !hard_level
        enemy:
            - rat
            - snake
            - dragon
        enemy_count: 10
''', Loader=yaml.Loader )



