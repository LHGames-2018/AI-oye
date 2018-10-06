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

        upgradeList = StorageHelper.read("upgradeList")
        if (upgradeList == None):
            upgradeList = []

            upgradeList.append((UpgradeType.CarryingCapacity, 10000))
            upgradeList.append((UpgradeType.CollectingSpeed, 10000))
            upgradeList.append((UpgradeType.CarryingCapacity, 15000))
            upgradeList.append((UpgradeType.CollectingSpeed, 15000))
            upgradeList.append((UpgradeType.AttackPower, 10000))
            upgradeList.append((UpgradeType.Defence, 10000))
            upgradeList.append((UpgradeType.MaximumHealth, 10000))
            upgradeList.append((UpgradeType.CollectingSpeed, 25000))
            upgradeList.append((UpgradeType.AttackPower, 15000))
            upgradeList.append((UpgradeType.CarryingCapacity, 25000))
            upgradeList.append((UpgradeType.Defence, 15000))
            upgradeList.append((UpgradeType.MaximumHealth, 15000))
            upgradeList.append((UpgradeType.AttackPower, 25000))
            upgradeList.append((UpgradeType.Defence, 25000))
            upgradeList.append((UpgradeType.MaximumHealth, 25000))
            upgradeList.append((UpgradeType.AttackPower, 50000))
            upgradeList.append((UpgradeType.Defence, 50000))
            upgradeList.append((UpgradeType.MaximumHealth, 50000))
            upgradeList.append((UpgradeType.AttackPower, 100000))
            upgradeList.append((UpgradeType.Defence, 100000))
            upgradeList.append((UpgradeType.MaximumHealth, 100000))
            upgradeList.append((UpgradeType.CarryingCapacity, 50000))
            upgradeList.append((UpgradeType.CollectingSpeed, 50000))
            upgradeList.append((UpgradeType.CarryingCapacity, 100000))
            upgradeList.append((UpgradeType.CollectingSpeed, 100000))

            StorageHelper.write("upgradeList", upgradeList)

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        # Find closest player! True False
        enemy_pos = enemy_is_close(gameMap, self.PlayerInfo, visiblePlayers)
        if enemy_pos:
            return create_attack_action(enemy_pos)

        upgradeList = StorageHelper.read("upgradeList")

        if(self.PlayerInfo.HouseLocation == self.PlayerInfo.Position and upgradeList and self.PlayerInfo.TotalResources >= upgradeList[0][1]):
            upgrade = upgradeList.pop(0)
            StorageHelper.write("upgradeList", upgradeList)
            return create_upgrade_action(upgrade[0])


        if self.PlayerInfo.CarriedResources == self.PlayerInfo.CarryingCapacity:
            pos = find_next_pos(gameMap, self.PlayerInfo, self.PlayerInfo.HouseLocation)
            if pos - self.PlayerInfo.Position == Point(0,0):
                return self.get_move(self.PlayerInfo.Position, self.PlayerInfo.HouseLocation, gameMap)
            return create_move_action(pos - self.PlayerInfo.Position)

        closest_resource_pos = find_closest_resource(gameMap, self.PlayerInfo)
        if Point.Distance(self.PlayerInfo.Position, closest_resource_pos) == 1:
            return create_collect_action(Point(closest_resource_pos.x - self.PlayerInfo.Position.x, closest_resource_pos.y - self.PlayerInfo.Position.y))
            
        pos = find_next_pos(gameMap, self.PlayerInfo, closest_resource_pos, TileContent.Resource)
        if (pos == self.PlayerInfo.Position):
            pos = find_next_pos(gameMap, self.PlayerInfo, self.PlayerInfo.HouseLocation)
        return create_move_action(pos - self.PlayerInfo.Position)


    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def find_nearest(self, tile_content, gameMap):
        min_dist = 10000
        tile_to_go = None

        for idx,row in enumerate(gameMap.tiles):
            for idx2,tile in enumerate(row):
                if tile.TileContent == tile_content:
                    distance = abs(tile.Position.x) + abs(tile.Position.y)
                    if distance < min_dist:
                        tile_to_go = tile

        return tile_to_go

    def get_move(self, src, dest, gameMap):
        if src.x < dest.x and not self.next_to(src, TileContent.Wall, gameMap) == Point(1, 0) :
            return create_move_action(Point(1, 0))
        if src.x > dest.x and not self.next_to(src, TileContent.Wall, gameMap) == Point(-1, 0):
            return create_move_action(Point(-1, 0))
        if src.y < dest.y and not self.next_to(src, TileContent.Wall, gameMap) == Point(0, 1):
            return create_move_action(Point(0, 1))
        if src.y > dest.y and not self.next_to(src, TileContent.Wall, gameMap) == Point(0, -1):
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
   