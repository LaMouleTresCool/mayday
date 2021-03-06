# -*- coding: UTF-8 -*-

import pygame
from ScreenManager import ScreenManager
from Menu import Menu
  
def main():
  # initialize pygame
  pygame.init()
  screen = pygame.display.set_mode((800, 600))

  # set window title
  pygame.display.set_caption("Mayday")

  # set mouse visible
  pygame.mouse.set_visible(1)
  # set key repeat (copied from tutorial, not sure if needed)
  #pygame.key.set_repeat(1, 30)

  # create clock object used to limit the framerate
  clock = pygame.time.Clock()

  # create the screen manager
  screenManager = ScreenManager()

  screenManager.addScreen(Menu(), True)
 
  # main loop
  running = True
  while running:
    # limit to 30 fps
    clock.tick(30)
 
    # get all events
    for event in pygame.event.get():
      # quit game if quit event is registered
      if event.type == pygame.QUIT:
        running = False
      
      # other events are handed down to the screen
      screenManager.update(event)
 
    # draw stuff
    screenManager.draw(screen);

    # actually draw the stuff
    pygame.display.flip()
 
if __name__ == '__main__':
    
    main()
