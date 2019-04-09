# Most Familiar Path

Our focus is on an algorithmic approach that concentrates on user’s convenience by considering user’s preferred and least preferred routes.

The current underlying algorithm used for modern GPS systems uses Dijkstra’s Algorithm. Our plan is to tweak and modify the algorithm by implementing the Most Familiar Path approach.

Basic concept of the Most Familiar Path includes having weighted nodes based on how frequent or infrequent the user travels to that node. The more frequent the user travels to that node the lower the weight while infrequently visited nodes will increase in weight with a maximum ceiling. These weighted nodes will be taken into consideration while applying Dijkstra’s shortest path algorithm and ultimately provide the user with the most convenient path.

Read more of the proposal: [Proposal Paper](https://docs.google.com/document/d/1hHOxRtA2XjoJ1Yti2BtMLkfRRJ9BKJEtCIe2zL7d11U/edit?usp=sharing)

This basic skeleton is an implementation of a directed graph with 4 nodes with each node having a self-looping edge with a weight value.

![Node graph](https://i.postimg.cc/1RDRLj0p/Most-Familiar-Path-Demo.png)

As you can see, the shortest path without the self-loops with weights would be: A, B, C, D <br>
However, the shortest path after consider the self-loop edges with weights using the most familiar approach is: A, C, D

<br>
Inside the python code has all the documentation line by line.
<br>
<br>

To run this program, simply download this file. <br>
Navigate to the file through the commandline. <br>
To run the program, type in the commandline: python familiar_path_playground.py
