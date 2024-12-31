from pyamaze import maze, agent, COLOR, textLabel


def dijkstra(m, *h, start=None):
    if start is None:
        start = (m.rows, m.cols)
    hurdles = [(i.position, i.cost) for i in h]
    unvisited = {n: float('inf') for n in m.grid}
    unvisited[start] = 0
    visited = {}
    revPath = {}
    while unvisited:
        currCell = min(unvisited, key=unvisited.get)
        visited[currCell] = unvisited[currCell]
        if currCell == m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])

                if childCell in visited:
                    continue
                tempDist = unvisited[currCell] + 1
                for hurdle in hurdles:
                    if hurdle[0] == currCell:
                        tempDist += hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell] = tempDist
                    revPath[childCell] = currCell
        unvisited.pop(currCell)
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[revPath[cell]] = cell
        cell = revPath[cell]
    return fwdPath, visited[m._goal]


if __name__ == '__main__':
    m = maze(15, 15)
    m.CreateMaze(loopPercent=20, theme='light')
    m._win.title("DFS Maze Solver")

    h1 = agent(m, 4, 4, 'square', color=COLOR.cyan)
    h2 = agent(m, 4, 6, 'square', color=COLOR.cyan)
    h3 = agent(m, 4, 2, 'square', color=COLOR.cyan)
    h4 = agent(m, 7, 2, 'square', color=COLOR.cyan)

    h1.cost = 50
    h2.cost = 120
    h3.cost = 80
    h4.cost = 100

    path, c = dijkstra(m, h1, h2, h3, h4, start=(m.rows, m.cols))
    textLabel(m, 'Total Cost', c)

    a = agent(m, m.rows, m.cols, color=COLOR.blue, filled=True,
              footprints=True)
    m.tracePath({a: path})

    # m = maze(6, 6)
    # m.CreateMaze(1, 4, loopPercent=100, theme='light')
    # m._win.title("DFS Maze Solver")
    # h1 = agent(m, 4, 4, 'square', color=COLOR.cyan)
    # h2 = agent(m, 4, 6, 'square', color=COLOR.cyan)
    # h3 = agent(m, 4, 2, 'square', color=COLOR.cyan)
    # h4=agent(m,4,1,'square',color=COLOR.cyan)
    # h5=agent(m,4,3,'square',color=COLOR.cyan)
    # h6=agent(m,4,6,'square',color=COLOR.cyan)
    #
    # h1.cost = 50
    # h2.cost = 50
    # h3.cost = 50
    # h4.cost=50
    # h5.cost=50
    # h6.cost=50
    #
    # path, c = dijkstra(m, h1, h2, h3, start=(6, 1))
    # textLabel(m, 'Total Cost', c)
    #
    # a = agent(m, 6, 1, color=COLOR.blue, filled=True,
    #           footprints=True)
    # m.tracePath({a: path})

    m.run()
    
    
