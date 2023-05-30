
mapWidth = 5
mapHeight = 5
#is node passable - not block by wall or already visited
def canWalk(map, visited, x, y):
            return 0 <= x < len(map) and 0 <= y < len(map[0]) and \
                not (map[x][y] == '#' or visited[x][y])
                 


def findShortestPath(map, visited, i, j, targetNode, minCost=2^31 - 1, currentCost=0 ):
    #target node found
    if(i, j) == targetNode:
        # return min(currentCost, minCost)
        return currentCost
    
    #node visited
    visited[i][j] = 1

    #down
    if canWalk(map, visited, i + 1, j):
        minCost = findShortestPath(map, visited, i + 1, j, targetNode, minCost, currentCost + 1)

    #right
    if canWalk(map, visited, i, j + 1):
        minCost = findShortestPath(map, visited, i, j + 1, targetNode, minCost, currentCost + 1)

    #up
    if canWalk(map, visited, i -1, j):
        minCost = findShortestPath(map, visited, i - 1, j, targetNode, minCost, currentCost + 1)

    #left
    if canWalk(map, visited, i, j - 1):
        minCost = findShortestPath(map, visited, i, j - 1, targetNode, minCost, currentCost + 1)   

    visited[i][j] = 0
    return minCost  

def minPathLength(map, startNode, targetNode):
    #start node
    i, j = startNode

    #target node
    x, y = targetNode  

    if not map or len(map) == 0 or map[i][j] =='#' or map[x][y] == '#':
        return -1
    
    (M, N) = len(map), len(map[0])

    #track visited nodes
    visited = [[False for _ in range(N)] for _ in range(M)]

    minCost = findShortestPath(map, visited, i, j, targetNode)

    if minCost != 2^31 - 1:
        return minCost
    else:
        return -1
   
map = [
    ['.', '.','#','P','#'],
    ['.', '.','.','.','#'],
    ['.', '.','#','.','#'],
    ['.', '.','#','Q','#'],
    ['.', '.','#','#','#'],
]


startNode = (0, 3)
targetNode = (3, 3)
#3 - correct

#test case 0
# map = [
#     ['P', '.','#','.','#'],
#     ['.', '.','.','.','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','Q','#'],
#     ['.', '.','#','#','#'],
# ]

# startNode = (0, 0)
# targetNode = (3, 3)
#6 - correct




#TEST CASES - 
#Case 1: start node is target node
# map = [
#     ['.', '.','#','.','#'],
#     ['.', '.','.','.','#'],
#     ['.', '.','#','#','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','#','#'],
# ]



# startNode = (0,3)
# targetNode = (0,3)

#pass - returns shortest path as 0

#Case 2 - no path - blocked by walls
# map = [
#     ['.', '.','#','P','#'],
#     ['.', '.','.','.','#'],
#     ['.', '.','#','#','#'],
#     ['.', '.','#','Q','#'],
#     ['.', '.','#','#','#'],
# ]


# startNode = (0, 3)
# targetNode = (3, 3)
# pass - no path available - correct

#case 3 - target node is not within map
# map = [
#     ['.', '.','#','P','#'],
#     ['.', '.','.','.','#'],
#     ['.', '.','#','#','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','#','#'],
# ]

# startNode = (0, 3)
# targetNode = (1, -1)

#no path available - correct, target off map

#case 4 - start node not on map
# map = [
#     ['.', '.','#','.','#'],
#     ['.', '.','.','.','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','Q','#'],
#     ['.', '.','#','#','#'],
# ]



# startNode = (-1, 3)
# targetNode = (3, 3)

#pass - no path available - correct, start off map


#case 5 - start and target nodes off map
# map = [
#     ['.', '.','#','.','#'],
#     ['.', '.','.','.','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','#','#'],
# ]



# startNode = (-1, 3)
# targetNode = (3, -1)

#pass - no paths available - correct

#case 6 - target directly below start
# map = [
#     ['.', '.','#','P','#'],
#     ['.', '.','.','Q','#'],
#     ['.', '.','#','#','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','#','#'],
# ]



# startNode = (0, 3)
# targetNode = (1, 3)
#pass - shortest path is 1 - correct

#case 6 - target is above start node
# map = [
#     ['.', '.','#','Q','#'],
#     ['.', '.','.','P','#'],
#     ['.', '.','#','#','#'],
#     ['.', '.','#','.','#'],
#     ['.', '.','#','#','#'],
# ]



# startNode = (1, 3)
# targetNode = (0, 3)
# fail - does not move straight up, uses left, up, right





minCost = minPathLength(map, startNode, targetNode)



if minCost != -1:
    print(minCost, "is the shortest path")
else:
    print("No path available")

