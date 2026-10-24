import pygame

class Button():
    def __init__(self,x,y,image,hover_image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.hover_image = hover_image

    def draw(self,WIN):

        action = False

        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if self.rect.collidepoint(position):
            WIN.blit(self.hover_image,(self.rect.x,self.rect.y))
        else:
            WIN.blit(self.image,(self.rect.x,self.rect.y))

        return action