from pyamaze.pyamaze import maze, agent, COLOR, textLabel


def BFS(m):
    start = (m.rows, m.cols)
    possible_cells = [start]
    visited_cells = [start]
    bfsPath = {}
    bSearch = []
    while len(possible_cells) > 0:
        current_Cell = possible_cells.pop(0)
        if current_Cell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[current_Cell][d]:
                if d == 'E':
                    NEXT_Cell = (current_Cell[0], current_Cell[1] + 1)
                elif d == 'W':
                    NEXT_Cell = (current_Cell[0], current_Cell[1] - 1)
                elif d == 'N':
                    NEXT_Cell = (current_Cell[0] - 1, current_Cell[1])
                elif d == 'S':
                    NEXT_Cell = (current_Cell[0] + 1, current_Cell[1])
                if NEXT_Cell in visited_cells:
                    continue
                possible_cells.append(NEXT_Cell)
                visited_cells.append(NEXT_Cell)
                bfsPath[NEXT_Cell] = current_Cell
                bSearch.append(NEXT_Cell)
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return bSearch, bfsPath, fwdPath


if __name__ == '__main__':
    m = maze(20, 20)
    m.CreateMaze(loopPercent=20, theme='light')
    m._win.title("BFS Maze Solver")
    bSearch, bfsPath, fwdPath = BFS(m)
    a = agent(m, footprints=True, color=COLOR.cyan, shape='square', filled=True)
    b = agent(m, footprints=True, color=COLOR.blue, shape='arrow', filled=False)
    c = agent(m, 1, 1, footprints=True, color=COLOR.green, shape='square', filled=True, goal=(m.rows, m.cols))
    l = textLabel(m, 'Length of Shortest Path', len(fwdPath) + 1)
    m.tracePath({a: bSearch}, delay=100)
    m.tracePath({c: bfsPath}, delay=100)
    m.tracePath({b: fwdPath}, delay=100)

    m.run()
