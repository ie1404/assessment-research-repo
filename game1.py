import pygame
import random

from pygame.locals import*
WIDTH=800
HEIGHT=600
TILE_SIZE=50
ROWS=4
COLS=4
FPS=30
empty_tile_pos = (ROWS - 1, COLS - 1)
none=None

board_width = COLS * TILE_SIZE
board_height = ROWS * TILE_SIZE
board_x = (WIDTH - board_width) // 2
board_y = (HEIGHT - board_height) // 2

# initialize Pygame
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()

# Tile class
class Tile:
    def __init__(self,value,row,col):
        self.value=value
        self.row=row
        self.col=col

    def draw(self):
        # Draw tile on screen
        recta=pygame.Rect(self.col*TILE_SIZE,self.row*TILE_SIZE,TILE_SIZE,TILE_SIZE)
        pygame.draw.rect(screen, (255, 255, 255), recta)
        
        font = pygame.font.Font(None, 50)  
        text_surf=font.render(str(self.value),True,(0,0,0))
        print(type(text_surf))
        text_rect=text_surf.get_rect()
        text_rect.center=recta.center
        
        screen.blit(text_surf, text_rect)
        

# game board
board=[]
for row in range(ROWS):
    board.append([])
    for col in range(COLS):
        board[row].append(Tile(row * COLS + col + 1, row, col))
board[ROWS - 1][COLS - 1] = Tile(None, ROWS - 1, COLS - 1)

for row in range(ROWS):
    board.append([])
    for col in range(COLS):
        if row == empty_tile_pos[0] and col == empty_tile_pos[1]:
            board[row].append(Tile(None, row, col))
        else:
            board[row].append(Tile(row * COLS + col + 1, row, col))


# Find the position of the empty tile
def find_empty_tile(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col].value is None:
                return row, col

# Swap two tiles on the game board
def swap_tiles(board, row1, col1, row2, col2):
    temp = board[row1][col1]
    board[row1][col1] = board[row2][col2]
    board[row2][col2] = temp
    
    # Update positions of the swapped tiles
    board[row1][col1].row = row1
    board[row1][col1].col = col1
    board[row2][col2].row = row2
    board[row2][col2].col = col2



# loop
running = True
while running:
    screen.fill((0, 50, 250))
    #
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # Move tile to the left
                print("a")
                empty_row, empty_col = find_empty_tile(board)
                if empty_col > 0:
                    swap_tiles(board, empty_row, empty_col, empty_row, empty_col - 1)
            elif event.key == pygame.K_d:
                print("d")
                # Move tile to the right
                empty_row, empty_col = find_empty_tile(board)
                if empty_col < COLS - 1:
                    swap_tiles(board, empty_row, empty_col, empty_row, empty_col + 1)
            elif event.key == pygame.K_w:
                # Move tile up
                print("w")
                empty_row, empty_col = find_empty_tile(board)
                if empty_row > 0:
                    swap_tiles(board, empty_row, empty_col, empty_row - 1, empty_col)
            elif event.key == pygame.K_s:
                # Move tile down
                print("s")
                empty_row, empty_col = find_empty_tile(board)
                if empty_row < ROWS - 1:
                    swap_tiles(board, empty_row, empty_col, empty_row + 1, empty_col)
        
   
    # Draw board
    board_surface = pygame.Surface((board_width, board_height))
    board_surface.fill((0, 255, 255))
    for row in range(ROWS):
        for col in range(COLS):
            tile_x=col*TILE_SIZE
            tile_y=row*TILE_SIZE
            tile = board[row][col]
            if tile.value:
                tile.draw()

    # Draw board surface on screen
    screen.fill((0, 0, 0))
    screen.blit(board_surface, (board_x, board_y))
    pygame.display.flip()


    # Limit frame rate
    clock.tick(FPS)