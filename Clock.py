
import pygame #Import pygame
import math
import datetime as dt
#Start up pygame
pygame.init()
pygame.font.init
pygame.display.set_caption("Rolex 2024")
screen = pygame.display.set_mode((1000, 750)) #Set display size
screen.fill((255, 255, 255)) #Fill screen with background color
#Making variables for the diffrent colors i will use
#Draw clock center circle
center = (400, 400)
#Set x/y height & width of center
x_cent, y_cent=1000//2, 750//2
center = (x_cent, y_cent)

#Make a funktion for the watch so i can run it in the loob so it updates constantly
def clock(screen, center):
    
    screen.fill((255, 255, 255)) #Fill screen with background color
    #Making variables for the diffrent colors i will use
    white = (255, 255, 255)
    black = (0, 0, 0)
    rolex_gold = (163, 126, 44)
    rolex_green = (0, 96, 57)
    silver = (192, 192, 192)
    red = (255, 0, 0)
    #Draw outerrim
    pygame.draw.circle(screen, silver, center, 350)

    #styling the watch with the green rolex backplate
    pygame.draw.circle(screen, black, center, 300)
    pygame.draw.circle(screen, rolex_green, center, 290)

    #Draw minute markings on back plate
    numb_lines = 12*5
    radius = 290
    for i in range(numb_lines):
        angle = 2*3.14*i/numb_lines
        end_x = x_cent + radius * math.cos(angle)
        end_y = y_cent + radius * math.sin(angle)
        pygame.draw.line(screen, rolex_gold, (x_cent, y_cent), (end_x, end_y), 3)
        
    #Cover cicle for minute markings
    pygame.draw.circle(screen, rolex_green, center, 270)

    #Drawing the hour markings on the backplate of the clock
    numb_lines = 12
    radius = 290
    for i in range(numb_lines):
        angle = 2*3.14*i/numb_lines
        end_x = x_cent + radius * math.cos(angle)
        end_y = y_cent + radius * math.sin(angle)
        pygame.draw.line(screen, rolex_gold, (x_cent, y_cent), (end_x, end_y), 6)

    #Fatter line at the end of the hour markings, just for style
    radius = 255
    for i in range(numb_lines):
        angle = 2*3.14*i/numb_lines
        end_x = x_cent + radius * math.cos(angle)
        end_y = y_cent + radius * math.sin(angle)
        pygame.draw.line(screen, rolex_gold, (x_cent, y_cent), (end_x, end_y), 10)

    #Cover up circle
    pygame.draw.circle(screen, rolex_green, center, 250)
    
    #Making variables for the diffrent times, so i can use them when making the clock hands
    current_time = dt.datetime.now()
    second_time = current_time.second
    minute_time = current_time.minute
    hour_time = current_time.hour

    #Center circle for clock hands
    pygame.draw.circle(screen, rolex_gold, center, 10)
    

    
    #Drawing the 3 clock hands. They are all drawn from the center of the clock, given a lengt, and a rotation that depends on the time.
    #Seconds hand
    pygame.draw.line(screen, silver, center, position_calculater(second_time, center, 250, 360/60), 4)

    #Minut hand
    pygame.draw.line(screen, rolex_gold, center, position_calculater(minute_time, center, 230, 360/60), 6)

    #Hour hand
    pygame.draw.line(screen, rolex_gold, center, position_calculater(hour_time, center, 200, 360/12), 10)
    
#Make a function that calculates the position, of the diffrent hands at diffrent times.
def position_calculater(tid, center, radius, angle):
    
    x_calc = center[0]+radius*math.cos(math.radians(angle*(tid-15)))
    
    y_calc = center[1]+radius*math.sin(math.radians(angle*(tid-15)))
    
    return (x_calc, y_calc)


#Keep pygame running
run_flag = True
while run_flag is True:
    #Run the funktion "watch" run in the loob that keeps pygame running, so it updates constantly.
    clock(screen, center)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip()    
    