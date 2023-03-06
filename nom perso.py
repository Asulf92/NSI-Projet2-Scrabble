import pygame as pygame


def main():
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.SysFont('KAZYcase scrabble', 25)
    input_box = pygame.Rect(100, 100, 140, 32)
    activer = False
    text = ''
    continuer = True

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_box.collidepoint(event.pos): #Si on clique dans la case 
                    activer = not activer
            if event.type == pygame.KEYDOWN:
                if activer:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:

                        print(text) #QUOI FAIRE QUAND ENTRER

                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, (255,255,255))
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, (255,255,255), input_box, 2)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
