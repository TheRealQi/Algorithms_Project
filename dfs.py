from pyamaze.pyamaze import maze, agent, COLOR


def DFS(m):
    start = (m.rows, m.cols)
    stack = [start]
    visited = []
    dfsPath = {}
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            for d in 'ESNW':
                if m.maze_map[current][d]:
                    if d == 'E':
                        childCell = (current[0], current[1] + 1)
                    elif d == 'S':
                        childCell = (current[0] + 1, current[1])
                    elif d == 'N':
                        childCell = (current[0] - 1, current[1])
                    elif d == 'W':
                        childCell = (current[0], current[1] - 1)
                    if childCell not in visited:
                        stack.append(childCell)
                        dfsPath[childCell] = current
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath


if __name__ == '__main__':
    m = maze(20, 20)
    m.CreateMaze(loopPercent=20, theme="light")
    path = DFS(m)

    # Create agent at the start position (bottom-right corner)
    a = agent(m, m.rows, m.cols, footprints=True, color=COLOR.cyan)
    m.tracePath({a: path})

    m.run()
