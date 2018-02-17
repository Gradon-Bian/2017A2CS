## Gradon Bian S3C5 Opt1
## Spring Holiday Homework: "The Maze Runner"
## Using Recursion
## If from coordinate (x,y), it can go to the top-left corner of the maze (the Exit), return "Successful!"

maze=[[1,0,0,1,0,1],
      [1,1,1,1,1,0],
      [0,0,1,0,1,0],
      [0,1,1,1,0,0],
      [1,0,0,1,0,0],
      [1,0,0,0,0,1]]

def valid(maze,x,y):## Check if the maze is valid
    if (x>=0 and x<len(maze) and y>=0 and y<len(maze[0]) and maze[x][y]==1):
        return True
    else:
        return False

def walk(maze,x,y):
    
    if(x==0 and y==0):
        print("Successful!")
        return True
    
    if valid(maze,x,y)==False:
        return ("Invalid coordination")

    if valid(maze,x,y):
      #  print(x,y)   Track the steps
        maze[x][y]=2  
        
        if not walk(maze,x-1,y):
            maze[x][y]=1
        elif not walk(maze,x,y-1):
            maze[x][y]=1
        elif not walk(maze,x+1,y):
            maze[x][y]=1
        elif not walk(maze,x,y+1):
            maze[x][y]=1
        else:
            return False  
    return True


walk(maze,3,3)


