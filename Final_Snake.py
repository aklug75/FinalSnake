# import only system from os
from os import system, name
import sys
 
# import sleep to show output for some time period
# from time import sleep

import random

map_width = 10
map_height = 10
snake_tiles = [(0,9)]
fruit_tile = (5,5)
crash_tile = None
space_tiles = [(0,0),(1,0),(2,2),(4,3),(8,9),(8,9)]
empty_map_char = "."
snake_body_char = "S"
fruit_character = "Ø"
crash_character = "!"
space_char = "X"
score = 0

 
# Defines our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 
 
# Defines the draw_map
def draw_map():
  clear()

# Defines the top border of the map
  top_border = map_width

# If the snake crash the top border
  if crash_tile is not None and crash_tile[0] == -1:
    top_border = top_border[:crash_tile[0]+1] + crash_character + top_border[crash_tile[0]+1:]
  print()
  
  snake_rows = [t[1] for t in snake_tiles]
  for i in range(0, map_height):
    line = empty_map_char*map_width
   
# Is there a part of the snake in this row
    if i in snake_rows:

# Get all cols, where the snake body is
      filtered_tiles = filter(lambda tile: tile[1] == i, snake_tiles)
      snake_cols = sorted([t[0] for t in filtered_tiles])
      for c in snake_cols:
        line = line[:c+1] + snake_body_char + line[c+2:]

# Draw the fruit
    if i == fruit_tile[1]:
      line = line[:fruit_tile[0]+1] + fruit_character + line[fruit_tile[0]+2:]
# Draw the crash character (if there has been a crash)
    if crash_tile is not None and crash_tile[1] == i:
      line = line[:crash_tile[0]+1] + crash_character + line[crash_tile[0]+2:]
    print(line)
  
# Defines the bottom border
  bottom_border = map_width
  if crash_tile is not None and crash_tile[1] == map_height:
    bottom_border = bottom_border[:crash_tile[0]+1] + crash_character + bottom_border[crash_tile[0]+2:]
  print()
  
  print("Snake tiles: ", snake_tiles)
  print("Fruit: ", fruit_tile)
  print("Crash tile: ", crash_tile)

# Defines the input for the next move for north, east, south or the west directions
def check_input():
  next_move = ""
  while next_move not in ['n', 'e', 's', 'w']:
    next_move = input("Next move (n,e,s,w)?")
  return next_move
  
# Defines the move-directions north, east, south and west of the snake
def move_snake(direction):
  last_pos = snake_tiles[0]
  if direction == 'n':
    new_pos = (last_pos[0], last_pos[1]-1)
  elif direction == 's':
    new_pos = (last_pos[0], last_pos[1]+1)
  elif direction == 'w':
    new_pos = (last_pos[0]-1, last_pos[1])
  elif direction == 'e':
    new_pos = (last_pos[0]+1, last_pos[1])
  else:
    new_pos = (last_pos[0], last_pos[1])
    
  snake_tiles.insert(0, new_pos)
  
# Defines the collision from the snake with the fruit 
def detect_collision():
  global score, crash_tile
  snake_head = snake_tiles[0]
# Did the snake eat a fruit?
  if snake_head == fruit_tile:
    score += 1
    add_fruit()
    return
  else:
# If the snake didn't eat, delete the last snake segment
    snake_tiles.pop()
  if snake_head[0] <= -1 or snake_head[0] >= map_width or snake_head[1] <= -1 or snake_head[1] >= map_height:
     crash_tile = snake_head
     game_over()
     
# Defines game over  
def game_over():
  draw_map()
  print("Game over")
  sys.exit()
  
# Defines that add a random new fruit
def add_fruit():
  global fruit_tile
  fruit_tile = (random.randrange(map_width), random.randrange(map_height))

# Defines a game loop
def game_loop():
  while True:
    inp = check_input()
    move_snake(inp)
    detect_collision()
    draw_map()
    
    
random.seed()

# Defines the input definition for Map height
try:
  map_height = max(int(input("Map height (min=4)? ")), 4)
except ValueError:
  map_height = 10

# Defines a input definition for Map width  
try:
  map_width = max(int(input("Map width (min=4)? ")), 4)
except ValueError:
  map_width = 10
  
draw_map()
game_loop()
