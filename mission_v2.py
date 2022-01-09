# please mark the submission_v{int}.py with the highest
# version number as the final submission

# v1 was the first exercsie in porting the 
# example.py program into a new file to get a
# real understand how the program structure
# was informing what was going on when run

# v1 is incomplete as it doen not conform to  the requirements 
# from the task instructions in PDF, i.e. 1 enemy only

# references used in making this game
# used this for key input documentation: https://www.pygame.org/docs/ref/key.html

# this version of task is in a procedural programming style
# overall task requiremnts were met this time:
# enemy numbers are correct, player movement is there,
# and 'prize' sprite is used 

# begin by importing modules 
# python game-programming library
import pygame as pg
# built-in python library to help
# with random number generation
import random as rd

# next we instantiate out pygame instance
pg.init()

# now to declare paramater varaibles 
# for the size of our game window
window_width = 1080
window_height = 720
# instantiate our window
window = pg.display.set_mode((window_width, window_height))

# now to instantiate our game graphics
# for player, enemy, and prize
player = pg.image.load('player.jpg')
enemy_1 = pg.image.load('monster.jpg')
enemy_2 = pg.image.load('monster.jpg')
enemy_3 = pg.image.load('monster.jpg')
prize = pg.image.load('prize.jpg')

# boundary detection for our graphics
player_height = player.get_height()
player_width = player.get_width()

enemy_1_height = enemy_1.get_height()
enemy_1_width = enemy_1.get_width()

enemy_2_height = enemy_2.get_height()
enemy_2_width = enemy_2.get_width()

enemy_3_height = enemy_3.get_height()
enemy_3_width = enemy_3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

# initilaise the player sprite position
player_x = 100
player_y = 360

# initialise the enemy sprite positions
enemy_1_x = window_width - 180
enemy_1_y = rd.randint(0, window_height - enemy_1_height)

enemy_2_x = window_width - 180
enemy_2_y = rd.randint(0, window_height - enemy_2_height)

enemy_3_x = window_width - 180
enemy_3_y = rd.randint(0, window_height - enemy_3_height)

# initialise prize sprite position
prize_x = 540
prize_y = 360

# initilaise varibales to check key inputs
# left, right, up, down
key_up = False
key_down = False
key_right = False
key_left =  False

# initilaise game loop
# remain true unless game over 
# or quit() invoked
while 1:

    # clear window view
    window.fill(0)

    # draw all sprites in the positions we instantiated them in
    window.blit(player, (player_x, player_y))
    window.blit(enemy_1, (enemy_1_x, enemy_1_y))
    window.blit(enemy_2, (enemy_2_x, enemy_2_y))
    window.blit(enemy_3, (enemy_3_x, enemy_3_y))
    window.blit(prize, (prize_x, prize_y))

    # update pygame instance
    pg.display.flip()

    # instantiating a for loop where my guess
    # is the pygame package event method works
    # on continually appending the list of events
    # as they're declared by the user as their 
    # inputs are detected??? must research 
    for event in pg.event.get():

        # check if user has quit game
        if event.type == pg.QUIT:

            # if so, initiate program termination
            pg.quit()
            exit(0)
        
        # checkin the state of key presses
        # if keys are being pressed
        if event.type == pg.KEYDOWN:

            # now to differentiate betweeen the 
            # type of key down event (directions...)

            # up or down only
            if event.key == pg.K_UP:
                key_up = True
            if event.key == pg.K_DOWN:
                key_down = True
            if event.key ==  pg.K_RIGHT:
                key_right = True
            if event.key == pg.K_LEFT:
                key_left = True
            
        # now for the instances where keys
        # are not being pressed
        if event.type == pg.KEYUP:

            # again a branche for our various directions
            if event.key == pg.K_UP:
                key_up = False
            if event.key == pg.K_DOWN:
                key_down = False
            if event.key == pg.K_RIGHT:
                key_right = False
            if event.key == pg.K_LEFT:
                key_left = False

    # now that event decalration is being
    # tracked, we want our sprites to react
    # due to these input and eachother
    if key_up == True:
        # ensure sprite remains within window
        if player_y > 0:
            player_y -= 1.5

    if key_down == True:
        # ensure sprite remains within window
        if player_y < (window_height - player_height):
            player_y += 1.5

    if key_right == True:
        # ensure sprite remains within window
        if player_x < (window_width - player_width):
            player_x += 1.5
    
    if key_left == True:
        # ensure sprite remains within window
        if player_x > 0:
            player_x -= 1.5

    # collision checks to define endgame scenarios
    # collide with enemy: lose
    # collide with prize: win

    # must defire hitboxes for out sprites
    # start with player box
    player_box = pg.Rect(player.get_rect())

    # now to defien the player box in relation 
    # to the player position (will do the same for other sprites)
    # setting the attributes next for player box

    player_box.top = player_y
    player_box.left = player_x

    # enemy box settings

    enemy_1_box = pg.Rect(enemy_1.get_rect())

    enemy_1_box.top = enemy_1_y
    enemy_1_box.left = enemy_1_x

    enemy_2_box = pg.Rect(enemy_2.get_rect())

    enemy_2_box.top = enemy_2_y
    enemy_2_box.left = enemy_2_x

    enemy_3_box = pg.Rect(enemy_3.get_rect())

    enemy_3_box.top = enemy_3_y
    enemy_3_box.left = enemy_3_x

    # same for prize settings

    prize_box = pg.Rect(prize.get_rect())

    prize_box.top = prize_y
    prize_box.left = prize_x

    # now to difine our box collision conditions
    # and therefore the endgame states of this program

    if player_box.colliderect(enemy_1_box):

        # output message to user
        print('\nYou were vanquished by Evil :(\n')

        # end game and quit
        pg.quit()
        exit(0)
    
    elif player_box.colliderect(enemy_2_box):

        # output message to user
        print('\nYou were vanquished by Evil :(\n')

        # end game and quit
        pg.quit()
        exit(0)
    
    elif player_box.colliderect(enemy_3_box):

        # output message to user
        print('\nYou were vanquished by Evil :(\n')

        # end game and quit
        pg.quit()
        exit(0)
    
    elif player_box.colliderect(prize_box):

        # output message to user
        print('\nYou reached the Artifact and vanquished Evil :)\n')

        # end game and quit
        pg.quit()
        exit(0)
    
    # logic for enemies to approch player

    enemy_1_x -= 2
    enemy_2_x -= 0.75
    enemy_3_x -= 1.35
