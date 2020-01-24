# amazing

Your mission, should you choose to accept it, is to train an "amazing" neural network to solve mazes.

You are provided an infinite maze dataset, and are expected to write the (a) training and (b) model architecture which takes ASCII mazes and plots the correct paths through them.

All the details of how you do this, including the choice of loss function, are up to you.  Please elaborate on your solution in a short writeup, and have fun!

Feel free to ask James (james.knighton@doc.ai) if you have any questions.

```
+ - + - + - + - - - - - + - - - + - - - + - + - - - - - - S - - + - + - - - +
|   |   |   |           |       |       |   |     9 9 9 9 9     |   |       |
|   |   |   |   |   - - +   + - +   + - +   + - + 9 + - - - - - +   |   |   |
|   |   |   |   |           |       |       |   | 9 |           |   |   |   |
|   |   |   + - +   |   - - + - +   + - -   |   | 9 + - +   + - +   |   + - +
|           |   |   |           |   |       |   | 9 |   |   |               |
+ - -   + - +   + - +   - - + - +   + - +   |   | 9 |   |   + - -   - - +   |
|       |   |               |       |   |   |   | 9                     |   |
|   - - +   + - + - +   - - + - +   |   |   |   | 9 - - - - - - +   - - + - +
|       |       |   |       |   |           | 9 9 9             |       |   |
|   + - +   + - +   |   + - +   |   - - - - + 9 |   |   - - + - + - - - +   |
|   |       |   |       |   | 9 9 9 9 9 9 9 9 9 |   |       |           |   |
|   + - +   |   + - +   |   | 9 |   |   |   - - +   |   |   + - -   - - +   |
|       |   |   |   |   |   | 9 |   |   |       |   |   |   |               |
|   - - +   |   |   |   |   | 9 + - +   + - + - +   + - + - +   |   + - +   |
|                   |     9 9 9     |   |   |                   |   |   |   |
|   + - + - +   - - + - + 9 - - + - + - +   + - + - + - -   - - + - +   |   |
|   |   |   |       |   | 9     |           |   |   |               |   |   |
|   |   |   + - - - +   | 9 + - + - +   - - +   |   |   |   + - +   |   + - +
|     9 9 9 9 9 9 9 9 9 9 9 |       |       |       |   |   |   |   |       |
+ - + 9 |   + - +   + - +   + - -   |   |   |   |   + - + - +   + - +   + - +
|   | 9 |   |   |   |   |   |           |   |   |   |       |   |   |   |   |
|   | 9 + - +   + - +   + - +   |   - - + - +   + - +   - - +   |   |   |   |
|     9             |   |   |   |       |   |                               |
|   | 9 - - + - - - +   |   + - +   - - +   |   + - + - +   + - -   - - +   |
|   | 9 9 9 |       |       |                   |   |   |   |           |   |
+ - + - + 9 |   - - +   - - +   - - + - +   - - +   |   + - + - +   |   + - +
|       | 9 9 9 9 9 9 9 9 9 9 9 9 9 |   |               |       |   |       |
|   - - +   + - +   + - +   - - + 9 |   |   |   |   + - +   |   |   + - -   |
|       |   |   |   |   |       | 9     |   |   |   |       |   |   |       |
|   - - +   |   + - +   + - - - + 9 - - + - + - + - +   + - + - + - + - +   |
|                       |         9 9 9 |       |       |   |   |       |   |
|   |   + - +   - - - - + - - - + - - 9 |   - - +   |   |   |   |   - - +   |
|   |   |   |           |       |     9             |           |       |   |
+ - +   |   + - - - - - +   - - + - - 9 |   |   - - +   |   - - +   - - + - +
|                               |     9 |   |       |   |               |   |
|   |   |   - - +   - - +   - - + - + 9 + - + - +   |   + - +   |   - - +   |
|   |   |       |       |           | 9         |   |       |   |           |
+ - + - + - - - + - - - + - - - - - + E - - - - + - + - - - + - + - - - - - + 
```
