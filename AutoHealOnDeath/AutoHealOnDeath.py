import sys

sys.path.append("../..")

from Level import Unit, Tags
from Consumables import HealPotSpell

print("[AutoHealOnDeath] mod loaded")


def kill_w_autoheal_deco(kill):
    def kill_w_autoheal(self, damage_event=None, trigger_death_event=True):
        healpot_item = next(
            (item for item in self.items if item.name == "Healing Potion"), None
        )
        if healpot_item is not None:
            self.cur_hp = 1
            self.level.deal_damage(
                self.x, self.y, -self.max_hp, Tags.Heal, HealPotSpell()
            )
            self.items.remove(healpot_item)
            return
        kill(self, damage_event, trigger_death_event)

    return kill_w_autoheal


Unit.kill = kill_w_autoheal_deco(Unit.kill)
