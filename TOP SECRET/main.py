import pygame
import os 
from video import Video
import time

pygame.init()
timer = pygame.time.Clock()
pygame.mixer.init()      

pygame.mixer.music.load("her.mp3")

font = pygame.font.Font("Comic Sans.ttf", 26)

screen = pygame.display.set_mode([1200, 600])
pygame.display.set_caption("Фанфік")

massages = ["                                                     Глава Перша",
            "(Поліна приходить додому, а Віка вже накрила на стіл)",
             "Віка: О Привіт Поліно нарешті ти приїхала!",
             "Поліна: Привіт та просто трохи затрималася у відрядженні",
             "(Віка підходить до Поліни і цілує її в губи)",
             "Поліна: та ну тобі, перестань",
             "Віка: гаразд пішли їсти (Їдять)",
             "Віка: до речі а що ти мені подаруєш на день народження?",
             "Поліна: а так завтра я піду за ним на весь день, пробач що не встигла забрати",
             "Віка: та ні нічого",
             "Поліна: Ти в мене найкраща",
             "Віка: ага",
             "(Уже всі поїли і пішли спати. Наступного дня)",
             "Поліна: з днем народження Віка!",
             "Віка: дякую!",
             "Поліна: гаразд я піду",
             "Віка: так давай (Поліна йде)",
             "Віка: ура могу позвать Сону н. (Вика звонит Сони н)",
             "Віка: альо",
             "Соня н: альо",
             "Віка: привіт приїжджай до мене, сьогодні Поліни не буде",
             "Соня н: скоро буду",
             "(Тим часом у Поліни)",
             "Поліна: ну що ж давай до тебе",
             "Соня т: так давай (Їдуть до соні т)",
             "(Приїжджає до соні т і соня т сідає в машину)",
             "Соня т: привіт",
             "Поліна: привіт як справи (збентежено подивилася на соню т)",
             "Соня т: нормально(теж збентежено подивилася на Поліну)",
             "(Сидять і дивляться один на одного)",
             "(Поліна Різко наблизилася до Соні т і бере її в засос)",
             "(Це було приблизно 2-3 хвилини)",
             "(Полина положила руку на талию и соня т ее отлкнула)",
             "                                            Кінець Першої Глави"
             ]

snip = font.render("", True, "white")

counter = 0
speed = 3
active_massage = 0
message = massages[active_massage]
done = False

run = True
while run:
    screen.fill("#006633")
    timer.tick(60)
#    pygame.draw.rect(screen, "#006633", [0, 300, 300, 600])
#    pygame.draw.rect(screen, "#006634", [38, 40, 200, 200])

    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(100)
    
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and done and active_massage < len(massages) - 1:
            active_massage += 1
            done = False
            message = massages[active_massage]
            counter = 0

    snip = font.render(message[0:counter//speed], True, "#ccc578")
    screen.blit(snip, (60, 200))
    
    
    pygame.display.flip()
pygame.quit()