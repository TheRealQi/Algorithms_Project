from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue


def dijkstra(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    open = PriorityQueue()
    open.put((0, start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    searchPath = [start]
    while not open.empty():
        currCell = open.get()[1]
        searchPath.append(currCell)
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                temp_g_score = g_score[currCell] + 1
                if temp_g_score < g_score[childCell]:
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    open.put((g_score[childCell], childCell))
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return searchPath, aPath, fwdPath


if __name__ == '__main__':
    m = maze(20, 20)
    m.CreateMaze(loopPercent=20, theme='light')
    searchPath, aPath, fwdPath = dijkstra(m)
    a = agent(m, footprints=True, color=COLOR.blue, filled=True)
    b = agent(m, 1, 1, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))
    c = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({a: searchPath}, delay=60)
    m.tracePath({b: aPath}, delay=60)
    m.tracePath({c: fwdPath}, delay=60)
    l = textLabel(m, 'Dijkstra Path Length', len(fwdPath) + 1)
    l = textLabel(m, 'Dijkstra Search Length', len(searchPath))
    m.run()
