from pyamaze import maze, agent, COLOR
def DFS(m):
    start=(m.rows-2,m.cols-2)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSearch=[start] 

    while len(frontier)>0:
        currCell=frontier.pop()

        if currCell==(1,1):
            break
        for d in 'WNSE':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
                dSearch.append(childCell)
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSearch, dfsPath, fwdPath 


if __name__=='__main__':
    m=maze(15,15)
    m.CreateMaze()
    path=DFS(m)
    a=agent(m,shape="arrow",footprints=True,filled=True)
    m.tracePath({a:path} , delay=50)

    m.run()
