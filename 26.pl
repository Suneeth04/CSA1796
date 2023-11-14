% Define the fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(lemon, yellow).
fruit_color(blueberry, blue).
fruit_color(strawberry, red).
fruit_color(kiwi, green).

% Define a predicate to find the color of a fruit
find_fruit_color(Fruit, Color) :- fruit_color(Fruit, Color).

% Define a predicate to find all fruits of a given color (backtracking)
find_fruits_of_color(Color, Fruits) :- findall(Fruit, fruit_color(Fruit, Color), Fruits).
