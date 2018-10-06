import numpy
from helper.structs import *
from helper.tile import *
from heapq import *

def is_resource(tile):
    return tile.TileContent == TileContent.Resource

def find_closest_resource(gameMap, player):
    closest_so_far = None
    closest_dist = 100000000
    for row in gameMap.tiles:
        for tile in row:
            tile_pos = Point(tile.Position.x, tile.Position.y)
            resource_dist =  Point.Distance(player.Position, tile_pos)
            if is_resource(tile) and resource_dist < closest_dist:
                closest_so_far = tile_pos
                closest_dist = resource_dist
    return closest_so_far

def has_reached_goal(player, goal, reached_dist = 0):
    return Point.Distance(player.Position, goal) == reached_dist

def find_next_pos(gameMap, player, goal):
    #weights = global_map.get_weights()
    # print 'Weights: ' + str(weights)

    if player.Position == goal:
        return goal

    start = (player.Position.x, player.Position.y)
    goal = (goal.x, goal.y)

    path = a_star(gameMap, start, goal)
    #path = a_star(gameMap.tiles, start, goal)
    # print 'Path: ' + str(path)

    # No path found
    if not path:
        return player.Position

    # Already there
    if len(path) == 0:
        return goal

    next_pos = Point(path[-1][0], path[-1][1])
    return next_pos

def needs_resource(player):
    return player.CarriedRessources != player.CarryingCapacity


def _heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def a_star(array, start, goal):
    print("start", start)
    print("goal", goal)

    array = numpy.array(array)
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:_heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + _heuristic(current, neighbor)

            xmin = array[0][0].Position.x
            xmax = array[-1][-1].Position.x
            ymin = array[0][0].Position.y
            ymax = array[-1][-1].Position.y

            if xmin <= neighbor[0] < xmax:
                if ymin <= neighbor[1] < ymax:
                    tile = array[neighbor[0]- xmin][neighbor[1] - ymin]
                    if tile.TileContent != TileContent.Empty and tile.TileContent != TileContent.House: # or blabla 
                        print("tile.TileContent", tile.TileContent)
                        continue
                else:
                    # array bound y walls
                    print("array bound y walls")
                    print("")
                    continue
            else:
                # array bound x walls
                print("array bound x walls")
                print("array.shape[0]", array.shape[0])

                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + _heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

def find_next_pos_resource(gameMap, player, goal):
    #weights = global_map.get_weights()
    # print 'Weights: ' + str(weights)

    if player.Position == goal:
        return goal

    start = (player.Position.x, player.Position.y)
    goal = (goal.x, goal.y)

    #path = a_star_resource(gameMap.tiles, start, goal)
    path = a_star_resource(gameMap, start, goal)
    # print 'Path: ' + str(path)

    # No path found
    if not path:
        return player.Position

    # Already there
    if len(path) == 0:
        return goal

    next_pos = Point(path[-1][0], path[-1][1])
    return next_pos

def a_star_resource(array, start, goal):
    print("start", start)
    print("goal", goal)

    array = numpy.array(array)
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:_heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + _heuristic(current, neighbor)

            xmin = array[0][0].Position.x
            xmax = array[-1][-1].Position.x
            ymin = array[0][0].Position.y
            ymax = array[-1][-1].Position.y

            if xmin <= neighbor[0] < xmax:
                if ymin <= neighbor[1] < ymax:
                    tile = array[neighbor[0]- xmin][neighbor[1] - ymin]
                    if tile.TileContent != TileContent.Empty and tile.TileContent != TileContent.House and tile.TileContent != TileContent.Resource: # or blabla 
                        print("tile.TileContent", tile.TileContent)
                        continue
                else:
                    # array bound y walls
                    print("array bound y walls")
                    print("")
                    continue
            else:
                # array bound x walls
                print("array bound x walls")
                print("array.shape[0]", array.shape[0])

                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + _heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False
