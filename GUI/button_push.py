# Def Push button
import pygame
import colour as cl


class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked =False

    #一般按鈕
    def draw(self,surface):
        action=False
        #底板
        pygame.draw.rect(surface,cl.black,(self.rect.x , self.rect.y , self.image.get_width(), self.image.get_height()))
        #邊框
        perimeter=pygame.draw.rect(surface,cl.white,(self.rect.x, self.rect.y ,self.image.get_width(), self.image.get_height()),3)
        #獲取鼠標位置
        pos = pygame.mouse.get_pos()

        #判斷鼠標是否點擊按鈕位置
        if perimeter.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                self.clicked =True
                action = True

        #鼠標沒有被點擊
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked= False

        #畫鼠標圖示到屏幕
        surface.blit(self.image,(self.rect.x,self.rect.y))

        return action

    #A 按鈕
    def A_draw(self,surface):
            action=False
            #底板
            pygame.draw.rect(surface,cl.Storm,(self.rect.x , self.rect.y , self.image.get_width(), self.image.get_height()))
            #邊框
            perimeter=pygame.draw.rect(surface,cl.Meltwater,(self.rect.x, self.rect.y ,self.image.get_width(), self.image.get_height()),3)
            #獲取鼠標位置
            pos = pygame.mouse.get_pos()

            #判斷鼠標是否點擊按鈕位置
            if perimeter.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                    self.clicked =True
                    action = True

            #鼠標沒有被點擊
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked= False

            #畫鼠標圖示到屏幕
            surface.blit(self.image,(self.rect.x,self.rect.y))

            return action

    #B 按鈕
    def B_draw(self,surface):
            action=False
            #底板
            pygame.draw.rect(surface,cl.Carnelian,(self.rect.x , self.rect.y , self.image.get_width(), self.image.get_height()))
            #邊框
            perimeter=pygame.draw.rect(surface,cl.Marshmallow,(self.rect.x, self.rect.y ,self.image.get_width(), self.image.get_height()),3)
            #獲取鼠標位置
            pos = pygame.mouse.get_pos()

            #判斷鼠標是否點擊按鈕位置
            if perimeter.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                    self.clicked =True
                    action = True

            #鼠標沒有被點擊
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked= False

            #畫鼠標圖示到屏幕
            surface.blit(self.image,(self.rect.x,self.rect.y))

            return action

    #C 按鈕
    def C_draw(self,surface):
            action=False
            #底板
            pygame.draw.rect(surface,cl.Gold,(self.rect.x , self.rect.y , self.image.get_width(), self.image.get_height()))
            #邊框
            perimeter=pygame.draw.rect(surface,cl.Parchment,(self.rect.x, self.rect.y ,self.image.get_width(), self.image.get_height()),3)
            #獲取鼠標位置
            pos = pygame.mouse.get_pos()

            #判斷鼠標是否點擊按鈕位置
            if perimeter.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                    self.clicked =True
                    action = True

            #鼠標沒有被點擊
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked= False

            #畫鼠標圖示到屏幕
            surface.blit(self.image,(self.rect.x,self.rect.y))

            return action

    #D 按鈕
    def D_draw(self,surface):
            action=False
            #底板
            pygame.draw.rect(surface,cl.Dark_Forest,(self.rect.x , self.rect.y , self.image.get_width(), self.image.get_height()))
            #邊框
            perimeter=pygame.draw.rect(surface,cl.Mint,(self.rect.x, self.rect.y ,self.image.get_width(), self.image.get_height()),3)
            #獲取鼠標位置
            pos = pygame.mouse.get_pos()

            #判斷鼠標是否點擊按鈕位置
            if perimeter.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                    self.clicked =True
                    action = True

            #鼠標沒有被點擊
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked= False

            #畫鼠標圖示到屏幕
            surface.blit(self.image,(self.rect.x,self.rect.y))

            return action
            
    #E 按鈕
    def E_draw(self,surface):
            action=False
            #底板
            pygame.draw.rect(surface,cl.Dusk,(self.rect.x , self.rect.y , self.image.get_width(), self.image.get_height()))
            #邊框
            perimeter=pygame.draw.rect(surface,cl.Buddleia,(self.rect.x, self.rect.y ,self.image.get_width(), self.image.get_height()),3)
            #獲取鼠標位置
            pos = pygame.mouse.get_pos()

            #判斷鼠標是否點擊按鈕位置
            if perimeter.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                    self.clicked =True
                    action = True

            #鼠標沒有被點擊
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked= False

            #畫鼠標圖示到屏幕
            surface.blit(self.image,(self.rect.x,self.rect.y))

            return action