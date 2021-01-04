# SearchAlgorithms
Implementation of different Search Algorithms for 2nd seminar at Artificial Intelligence.

Game
----

The idea is based on a simple game of moving cubes in a warehouse.
Main objective is to find a series of commands, that leads us into the Output state.
Given two text files (input, expected output), each containing a matrix of N rows and P coumns

Example:

![](https://github.com/klemen-1337/SearchAlgorithms/blob/master/Example.PNG)

Rules
-----

 - You can only use a series of commands **PRESTAVI** p, r (move from p-th column to r-th)
 - You can only take the top box from that column
 - If the r-th position is empty, put the box on the floor, otherwise put it on top of another box (if you can)
 - If the p-th position is empty, nothing happens
 
 


