# Oxbury Pathfind

Imagine representing a grid-shaped game map as a 2-dimensional array. Each value of this array is
boolean `true` or `false` representing whether that part of the map is passable (a floor) or blocked
(a wall).

Write a function that takes such a 2-dimensional array `A` and 2 vectors `P` and `Q`, with `0,0` being the top left corner of the map and returns the distance of the shortest path between those points, respecting the walls in the map.

eg. Given the map (where `.` is passable - `true`, and `#` is blocked - `false`)

```
. P . . .
. # # # .
. . . . .
. . Q . .
. . . . .
```

then `pathfind(A, P, Q)` should return `6`.

_Please avoid using libraries to implement the algorithmic side of this challenge, other libraries (such as PHPUnit or Jest for testing) are welcome._

## What to do

1. Clone/Fork this repo or create your own
2. Implement the function described above in any mainstream language you wish
3. Provide unit tests for your submission
4. Fill in the section(s) below

## Comments Section

<!---
Please fill in the sections below after you complete the challenge.
--->

### What I'm Pleased With
I am pleased that I found a solution that works for all but one of the test cases that I have presented to it. I am fairly pleased with the clarity of my code as I believe it it quite easy to follow and sections e.g. functions could be reused in future code. 

### What I Would Have Done With More Time
If I had more time, I would research or ask for support in adjusting my function so that it passes when the target is above thae starting point on the grid. I have just begun a chapter on pathfinding algorithms on my Into to Computer Science course, so I would implement and test dijkstra or other such algorithms or use them to edit my own function to pass the final test case. I would also find it interesting to use BFS, DFS dijkstra and A* on the same map and time each one. 
I would have investigated how to implement further tests using a library such as 'pytest.' (Testing is an area of my skill set I am working on developing). In the future, I would use libraries to present the code in an interesting way and to track the path as it moves through the maze. For future development purposes, I would like to implement this challenge into games. 
