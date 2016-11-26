"""Ninja vs Samurai: Attack + Block
https://www.codewars.com/kata/ninja-vs-samurai-attack-plus-block

Something is wrong with our Warrior class. All variable should initialize
properly and the attack method is not working as expected.

If properly set, it should correctly calculate the damage after an attack
(if the attacker position is == to the block position of the defender,
no damage; otherwise, the defender gets either 10 damage if hit "high" or
5 damage if it "low". If no block is set, the defender takes 5 **extra** damage
to his health.

For some reason, the health value is not being properly set. The following
shows an example of this code being used:

```python
ninja = Warrior('Hanzo Hattori')
samurai = Warrior('Ryōma Sakamoto')

samurai.block = 'l'
ninja.attack(samurai, 'h')
#samurai.health should be 90 now
```

The warriors must be able to fight to the bitter end, and good luck to the most
skilled!

Notice that health can't be below 0: once hit to 0 health, a warrior attribute
`deceased` becomes true; if hit again, the `zombie` attribute becomes true too!
"""

POSITION = {'high': 'h', 'low': 'l'}


class Warrior(object):
    """Game warrior representation"""

    def __init__(self, name):
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        # default guard is "", that is unguarded
        self.block = ""
        self.deceased = False
        self.zombie = False

    @staticmethod
    def attack(enemy, position):
        """Attack the enemy on the given position """
        damage = 0
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        if enemy.block != position:
            damage += 10 if position == POSITION['high'] else 5
        # and even more damage if the enemy is not blocking at all
        if enemy.block == "":
            damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        """Updates warrior health points"""
        # health cannot have negative values
        self.health = max(0, new_health)
        # if a warrior is set to 0 health he is dead
        if self.health == 0:
            self.deceased = True
            self.zombie = False
        # he would be a zombie only if he was already dead
        elif self.deceased:
            self.zombie = True
