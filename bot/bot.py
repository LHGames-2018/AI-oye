from helper import *


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




        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def get_move(self, src, dest):
        if src.x < dest.x:
            return create_move_action(Point(1, 0))
        if src.x > dest.x:
            return create_move_action(Point(-1, 0))
        if src.y < dest.y:
            return create_move_action(Point(0, 1))
        if src.y > dest.y:
            return create_move_action(Point(0, -1))

    def next_to(self, pos, tileContent, gameMap):
        if gameMap.getTileAt(Point(pos.x + 1, pos.y)).tileContent == tileContent:
            return Point(pos.x + 1, pos.y)
        if gameMap.getTileAt(Point(pos.x - 1, pos.y)).tileContent == tileContent:
            return Point(pos.x - 1, pos.y)
        if gameMap.getTileAt(Point(pos.x, pos.y + 1)).tileContent == tileContent:
            return Point(pos.x, pos.y + 1)
        if gameMap.getTileAt(Point(pos.x, pos.y - 1)).tileContent == tileContent:
            return Point(pos.x, pos.y - 1)
        return null