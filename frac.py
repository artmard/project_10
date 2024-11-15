import time
import pygame
import random

pygame.init() # инициализация библиотеки

# запись цветов интерфейса
white = (250, 235, 215)
dark_white=(255, 222, 173) 
black = (0, 0, 0)
red = (255, 0, 0)
dark_red = (139, 0, 0)
green = (0, 100, 0)
FireBrick=(178, 34, 34)
DarkOrange=(255, 140, 0)
GreenYellow=(34, 139, 34)
brown=(139, 69, 19)
# размеры поля    
dis_x=600
dis_y=dis_x
dis=pygame.display.set_mode((dis_x,dis_y)) # создаем игровое поле

# подготовка дисплея и запуск времени
pygame.display.update() # обновляем экран
pygame.display.set_caption('frac')
clock=pygame.time.Clock()

snake_size=1 # толщина змейки
snake_speed=10000 # скорость змейки
mx=0 # переменная для лучшего результата
txt_style=pygame.font.SysFont(None,40) # задание размера текста
def frac(snake_size,frac_list): # функция рисующая змейку
    for i in frac_list:
        pygame.draw.rect(dis, green, [i[0],i[1],snake_size,snake_size])
def massage(text,color): # функция выводящая сообщение
    msg=txt_style.render(text,True,color)
    dis.blit(msg,[dis_x/2-len(text)*6,dis_y/2-20])
def Your_score(score): # функция выводящая текущий результат
   value = txt_style.render("Your score: " + str(score), True, black)
   dis.blit(value, [0, 0])
def Your_record(score): # функция выводящая лучший результат
   value = txt_style.render("Your record: " + str(score), True, black)
   dis.blit(value, [0, 25])  
def pause(): # функция выводящая текущий результат
   value = txt_style.render("Pause" , True, black)
   dis.blit(value, [0, 0])    
def ma(snake_long): # функция определяющая лучший результат
    global mx
    if mx<snake_long:
                mx=snake_long    

      
def gameloop():
    game_end=False # флаг отвечающий за конец игры
    game_close=False # стартовое меню
    fl=False
    Pause=False
    dot1=[10,dis_y-40]
    dot2=[590,dis_y-40]
    dot3=[295,dis_y-570]
    dot4=[random.randrange(60,550,1),random.randrange(10,300,1)]
    snake_long=1 # длина змейки
    frac_list=[dot1,dot2,dot3,dot4] 
    
    
    while not game_end: # главный цикл, пока gama_end=False, игра продолжается
        
        if Pause: # цикл экрана меню
            pygame.display.update()
        while Pause==True:
            dis.fill(white)
            massage('Press A to continue game', black)
            pause()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a: # запуск новой игры
                        Pause=False
                if event.type==pygame.QUIT: # закрытие окна
                    pygame.quit() # деинициализация библиотеки
                    quit()
        if game_close: # цикл экрана меню
            massage('YOU LOSE', red)
            pygame.display.update()
            time.sleep(2)
            
        while game_close==True:
            dis.fill(white)
            massage('Press A to start game', black)
            Your_score(snake_long-1)
            Your_record(mx-1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a: # запуск новой игры
                        gameloop()
                if event.type==pygame.QUIT: # закрытие окна
                    pygame.quit() # деинициализация библиотеки
                    quit()    
        # цикл для перемещения змейки            
        for event in pygame.event.get(): # достаём все события из массива событий в библиотеке pygame. event.get() возвращает в терминал все события, которые происходят с игрой
            if event.type==pygame.QUIT: # закрытие окна
                pygame.quit() # деинициализация библиотеки
                quit()
            if event.type==pygame.KEYDOWN: # считывает нажато ли что-то на клавиатуре
                if event.key==pygame.K_ESCAPE: 
                        Pause=True    
        k=2    
        r=random.randint(1,3)
        if r==1:
            frac_list.append([(dot1[0]+frac_list[-1][0])/k,(dot1[1]+frac_list[-1][1])/k])
        elif r==2:
            frac_list.append([(dot2[0]+frac_list[-1][0])/k,(dot2[1]+frac_list[-1][1])/k])
        else:
            frac_list.append([(dot3[0]+frac_list[-1][0])/k,(dot3[1]+frac_list[-1][1])/k])
        frac(snake_size,frac_list)
        pygame.display.update() 
        
        
        
        ma(snake_long)
        
        dis.fill(white)
        clock.tick(snake_speed)       
gameloop()