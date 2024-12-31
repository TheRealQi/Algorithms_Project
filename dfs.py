from pyamaze.pyamaze import maze, agent, COLOR, textLabel


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
    m = maze(15, 15)
    m.CreateMaze(loopPercent=20, theme="light")
    m._win.title("DFS Maze Solver")
    fwdPath = DFS(m)
    a = agent(m, m.rows, m.cols, footprints=True, color=COLOR.cyan, shape='square', filled=True)
    l = textLabel(m, 'Length of Path', len(fwdPath) + 1)
    m.tracePath({a: fwdPath})

    m.run()
