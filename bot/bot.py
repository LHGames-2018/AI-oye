from helper import *
from bot.bot_utils import *
import os

class Bot:
    def __init__(self):
        # local 66 66
        # live 132 198

        #self.width = 133
        #self.height = 199
        
        # print(os.environ.get('IS_LOCAL'))
        # if (os.environ.get('IS_LOCAL')):
        self.width = 1000
        self.height = 1000


        self.GameMap = list()
        #self.GameMap = GameMap()
        for i in range(self.width):
            self.GameMap.append(list())
            for j in range(self.height):
                self.GameMap[i].append(Tile(TileContent.Empty, i, j))

        

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

        for row in gameMap.tiles:
            for tile in row:
                #print("tile.Position.x", tile.Position.x)
                #print("tile.Position.y", tile.Position.y)
                self.GameMap[tile.Position.x][tile.Position.y] = tile


        if self.PlayerInfo.CarriedResources == self.PlayerInfo.CarryingCapacity:
            pos = find_next_pos(self.GameMap, self.PlayerInfo, self.PlayerInfo.HouseLocation)
            return create_move_action(pos - self.PlayerInfo.Position)

        closest_resource_pos = find_closest_resource(gameMap, self.PlayerInfo)
        if Point.Distance(self.PlayerInfo.Position, closest_resource_pos) == 1:
            return create_collect_action(Point(closest_resource_pos.x - self.PlayerInfo.Position.x, closest_resource_pos.y - self.PlayerInfo.Position.y))
            
        pos = find_next_pos_resource(self.GameMap, self.PlayerInfo, closest_resource_pos)
        print("Player pos: ", self.PlayerInfo.Position)
        print("Pos: ", pos)
        if (pos == self.PlayerInfo.Position):
            pos = find_next_pos(self.GameMap, self.PlayerInfo, self.PlayerInfo.HouseLocation)

        return create_move_action(pos - self.PlayerInfo.Position)


    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def find_nearest(self,tile_content,gameMap):
        min_dist = 10000
        tile_to_go = None

        for idx,row in enumerate(gameMap.tiles):
            for idx2,tile in enumerate(row):
                if tile.TileContent == tile_content:
                    distance = abs(tile.Position.x) + abs(tile.Position.y)
                    if distance < min_dist:
                        tile_to_go = tile

        return tile_to_go

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
        if gameMap.getTileAt(Point(pos.x + 1, pos.y)) == tileContent:
            return Point(pos.x + 1, pos.y)
        if gameMap.getTileAt(Point(pos.x - 1, pos.y)) == tileContent:
            return Point(pos.x - 1, pos.y)
        if gameMap.getTileAt(Point(pos.x, pos.y + 1)) == tileContent:
            return Point(pos.x, pos.y + 1)
        if gameMap.getTileAt(Point(pos.x, pos.y - 1)) == tileContent:
            return Point(pos.x, pos.y - 1)
        return None