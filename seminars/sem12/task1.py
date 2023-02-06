# Улитка ползет по столбу высотой 12 м, днем на 2м вверх и ночью на 1м вниз. 
# На какой день она окажется на вершине"

# l = int(input('Введите высоту столба в метрах: '))
# h = int(input('Введите сколько метров за день проползает улитка вверх: '))
# w = int(input('Введите на сколько метров улитка сползает вниз: '))
# day = 0


def snail(height, speed_down=1,speed_up=2):
    first_height = height
    day=0
    height_old=height
    while(True):
        day+=1
        height-=speed_up
        if height<=0: return day
        height+=speed_down   
        if height>first_height or height==height_old:
            return 'Улитка никогда не заползет на столб'

print(snail(12,1,2))