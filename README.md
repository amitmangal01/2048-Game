# 2048-Game

In this article we will look python code and logic to design a 2048 game you have played very often in your smartphone. If you are not familiar with the game, it is highly recommended to first play the game so that you can understand the basic functioning of it.

 How to play 2048 :
1. There is a 4*4 grid which can be filled with any number. Initially two random cells are filled with 2 in it. Rest cells are empty.

2. we have to press any one of four keys to move up, down, left, or right. When we press any key, the elements of the cell move in that direction such that if any two identical numbers are contained in that particular row (in case of moving left or right) or column (in case of moving up and down) they get add up and extreme cell in that direction fill itself with that number and rest cells goes empty again.

3. After this grid compression any random empty cell gets itself filled with 2.

4. Following the above process we have to double the elements by adding up and make 2048 in any of the cell. If we are able to do that we wins.

5. But if during the game there is no empty cell left to be filled with a new 2, then the game goes over.

In above process you can see the snapshots from graphical user interface of 2048 game. But all the logic lies in the main code. So to solely understand the logic behind it we can assume the above grid to be a 4*4 matrix ( a list with four rows and four columns). You can see below the way to take input and output without GUI for the above game.

Example : 

Commands are as follows : 
'W' or 'w' : Move Up
'S' or 's' : Move Down
'A' or 'a' : Move Left
'D' or 'd' : Move Right

[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 2, 0]

Press the command : a
GAME NOT OVER
[0, 0, 0, 2]
[0, 0, 0, 0]
[0, 0, 0, 0]
[2, 0, 0, 0]

Press the command : s
GAME NOT OVER
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 2, 0]
[2, 0, 0, 2]

Press the command : d
GAME NOT OVER
[0, 0, 0, 0]
[0, 0, 0, 0]
[2, 0, 0, 2]
[0, 0, 0, 4]

Press the command : a
GAME NOT OVER
[0, 2, 0, 0]
[0, 0, 0, 0]
[4, 0, 0, 0]
[4, 0, 0, 0]

Press the command : s
GAME NOT OVER
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[8, 2, 0, 2]
.
.
.
And the series of input output will go on till we lose or win!


**Programming Approach : **

1. We will design each logic function such as we are performing a left swipe then we will use it for right swipe by reversing matrix and performing left swipe.
2. Moving up can be done by taking transpose then moving left.
3. Moving down can be done by taking transpose the moving right.
4. All the logic in the program are explained in detail in the comments. Highly recommended to go through all the comments.

We have two python files below, one is 2048.py which contains main driver code and the other is logic.py which contains all functions used. logic.py should be imported in 2048.py to use these functions. just place both the files in the same folder then run 2048.py will work perfectly.

