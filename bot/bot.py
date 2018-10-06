from helper import *
from bot.bot_utils import *


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        if self.PlayerInfo.CarriedResources == self.PlayerInfo.CarryingCapacity:
            pos = find_next_pos(gameMap, self.PlayerInfo.Position, self.PlayerInfo.HouseLocation)
            return create_move_action(pos)

        closest_resource_pos = find_closest_resource(gameMap, self.PlayerInfo.Position)
        if Point.Distance(self.PlayerInfo.Position, closest_resource_pos) == 1:
            return create_collect_action(Point(closest_resource_pos.x - self.PlayerInfo.Position.x, closest_resource_pos.y - self.PlayerInfo.Position.y))
            
        pos = find_next_pos(gameMap, self.PlayerInfo.Position, closest_resource_pos)
        return create_move_action(pos)

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
