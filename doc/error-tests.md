### Ошибка №1. 
__Описание__:  не совпали ожидаемые значения  
__Тест__: 1.1 в модуле add для метода Life.destroy()  
__Входные данные__: Life.img, const.life_img  
__Ожидаемый результат__: совпадение входных данных  
__Фактический результат__: sprites.Sprite object at 0x105e7ba10 != 'assets/heart.png'  
__Возможная причина__: попытка сравнить объект класса и строку  
__Cтатус__: исправлена 

### Ошибка №2
__Описание__:  не совпали ожидаемые значения  
__Тест__: 1.2 в модуле add для метода Life.destroy()  
__Входные данные__: Life.img, const.blank_life_img  
__Ожидаемый результат__: совпадение входных данных  
__Фактический результат__: sprites.Sprite object at 0x107558190 != 'assets/blank_life.png'  
__Возможная причина__: попытка сравнить объект класса и строку  
__Cтатус__: исправлена 
