import pygame

class TextBox:
    #Constructor
    def __init__(self, x, y, w, h, fontSize=24, maxLength=100, resizable=True, text='', textColor=(0,0,0), borderColor=(40,120,180), activeBorderColor=(200,0,0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = borderColor
        self.inactiveColor = borderColor
        self.textColor = textColor
        self.activeColor = activeBorderColor
        self.maxLength = maxLength
        self.resizable = resizable
        self.text = text
        self.fontSize= fontSize
        FONT = pygame.font.Font(None, self.fontSize)
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Detects when the user clicks on the textbox
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.activeColor
            else:
                self.active = False
                self.color = self.inactiveColor
 
 
 
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #Clear text box
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    #Remove last character
                    self.text = self.text[:-1]
                elif event.key in [pygame.K_TAB,pygame.K_ESCAPE]:
                    #Ignore = do nothing
                    pass
                else:
                    #Append character
                    if len(self.text) < self.maxLength:
                        self.text += event.unicode
                #Display text
                FONT = pygame.font.Font(None, self.fontSize)
                self.txt_surface = FONT.render(self.text, True, self.textColor)
 
    def update(self):
        # Resize the box if the text is too long.
        if self.resizable:
            width = max(200, self.txt_surface.get_width()+10)
            self.rect.w = width
 
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)