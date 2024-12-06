import sys

sys.path.append("../..")

from Level import Unit

print("[AutoHealOnDeath] mod loaded")


def kill_w_autoheal_deco(kill):
    def kill_w_autoheal(self, damage_event=None, trigger_death_event=True):
        if self.name == "Player":
            healpot_item = next(
                (item for item in self.items if item.name == "Healing Potion"), None
            )
            if (healpot_item is not None) and (healpot_item.quantity > 0):
                self.cur_hp = 1
                self.level.act_cast(self, healpot_item.spell, self.x, self.y)
                return
        kill(self, damage_event, trigger_death_event)

    return kill_w_autoheal


Unit.kill = kill_w_autoheal_deco(Unit.kill)
