import pygame


pygame.font.get_fonts()

text_colour =(255,255,255,)
button_colour =(0,0,170)
button_over_colour =(255,50,50)
button_width = 100
button_height = 50

button_rect = [(600() - 600)/2,
             screen.get_width()/2 - button_height/2,
             button_width, button_height]

button_font = pygame.font.SysFont('Verdana', 20)

button_text = button_font.render('QUIT', True, text_colour)

screen.fill((100, 100, 100))


game_over = False

while not game_over:
   for event in pygame.event.get():
       if event.type==pygame.QUIT:
           game_over=True

       if event.type == pygame.MOUSEBUTTONDOWN:
           x, y = event.pos

           if (button_rect[0] <= x <= button_rect[0] + button_rect[2] and
                   button_rect[1] <= y <= button_rect[1] + button_rect[3]):
               game_over = True


   pygame.draw.rect(screen, button_colour, button_rect)

   screen.blit(button_text, (button_rect[0] + (button_width - button_text.get_width()) / 2,
                             button_rect[1] + (button_height / 2 - button_text.get_height() / 2)))


   pygame.display.update()

pygame.quit()