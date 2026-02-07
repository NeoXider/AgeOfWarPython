"""
Билдер анимаций для “воинов”.

Делает `spritePro.Animation` и регистрирует в ней состояния (idle/walk/...).
"""

import spritePro as s

from game.domain import UnitType
from game.paths import PATHS

def _build_animation(sprite: s.Sprite, unit_type: UnitType) -> s.Animation:
    """Создаёт анимацию для юнита конкретного типа."""
    
    anim = s.Animation(owner_sprite=sprite)
     
    if unit_type == UnitType.MELEE:
        warrior_path = "Warrior1"
    else:
        warrior_path = "Warrior2"
    
    anim.add_state('idle', [
        PATHS.images_warrior + f'/{warrior_path}/Warrior_idle/Warrior_idle.png'
    ])
    
    anim.add_state('walk', [
        PATHS.images_warrior + f'/{warrior_path}/Warrior_walk/Warrior_walk1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_walk/Warrior_walk2.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_walk/Warrior_walk3.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_walk/Warrior_walk4.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_walk/Warrior_walk5.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_walk/Warrior_walk6.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_walk/Warrior_walk7.png',
    ])
    
    anim.add_state('atack', [
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_first_atack1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_first_atack2.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_first_atack3.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_first_atack4.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_second_atack1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_second_atack2.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_second_atack3.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_second_atack4.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_three_atack1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_three_atack2.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_three_atack3.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_atack/Warrior_three_atack4.png',
    ])
    
    anim.add_state('hurt', [
        PATHS.images_warrior + f'/{warrior_path}/Warrior_hurt/Warrior_hurt1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_hurt/Warrior_hurt2.png',
    ])
    
    anim.add_state('dead', [
        PATHS.images_warrior + f'/{warrior_path}/Warrior_dead/Warrior_dead1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_dead/Warrior_dead2.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_dead/Warrior_dead3.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_dead/Warrior_dead4.png',
    ])
    
    anim.add_state('protect', [
        PATHS.images_warrior + f'/{warrior_path}/Warrior_protect/Warrior_protect1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_protect/Warrior_protect2.png',
    ])
    
    anim.add_state('run', [
        PATHS.images_warrior + f'/{warrior_path}/Warrior_run/Warrior_run1.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_run/Warrior_run2.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_run/Warrior_run3.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_run/Warrior_run4.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_run/Warrior_run5.png',
        PATHS.images_warrior + f'/{warrior_path}/Warrior_run/Warrior_run6.png',
    ])
    
    return anim