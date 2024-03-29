[![GitHub Actions](https://github.com/rensffz/project/actions/workflows/main.yml/badge.svg)](https://github.com/rensffz/project/actions/workflows/main.yml)
[![Coverage Status](https://coveralls.io/repos/github/rensffz/project/badge.svg?branch=main)](https://coveralls.io/github/rensffz/project?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rensffz_project&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=rensffz_project)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=rensffz_project&metric=bugs)](https://sonarcloud.io/summary/new_code?id=rensffz_project)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=rensffz_project&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=rensffz_project)

# Урожай

## Цель проекта:

Разработка компьютерной игры, позволяющей игроку управлять персонажем и контролировать его действия.

## Мотивация:

Получить навыки создания программного продукта.

## Общие сведения:

Программа "Урожай" представляет собой компьютерную игру, реализующую управление персонажем и его передвижение.
Игра написана на языке Python с использованием библиотек pygame (для реализации графического интерфейса) и random (для выбора случайных значений в ходе игры, где это будет необходимо).

## Программа представлена следующими объектами:

    - модуль main.py - основной модуль игры;
    - модуль game.py - модуль, который определяет класс Game для управления игрой, инициализации игровых объектов и отрисовки экрана, а также функцию инициализации и главный игровой цикл;
    - модуль add.py - модуль, который определяет классы Resource, Life и Environment для дополнительных игровых объектов (ресурсов и жизней) и элементов экрана;
    - модуль characters.py - модуль, который определяет классы Main и Enemy для игровых персонажей и их поведения;
    - модуль sprites.py - модуль, который определяет класс Sprite для загрузки и хранения спрайтов игровых объектов;
    - модуль utils.py -  модуль, который содержит вспомогательные функции;
    - модуль constants.py - модуль, содержащий константы для игры;
    
    - папка assets, содержащая изображения игровых объектов в формате png и шрифт в формате ttf
    

## Функциональности проекта:

После запуска программы, перед началом игры пользователю предоставляется возможность прочитать инструкцию. Игроку будет предложено собрать определённое количество ресурсов за отведённое время, не столкнувшись с "врагом". Также игрок имеет фиксированное количество жизней, которое уменьшается при столкновении (после того, как исчезнет последняя, игра завершается с проигрышем).

С момента запуска игры (путём нажатия клавиши SPACE) начинается обратный отсчёт, а также игра автоматически реализует передвижение вражеских объектов по игровому полю. При столкновении игрока с одним из них, игра начинается заново, а количество оставшихся жизней уменьшается. Как только все жизни закончатся, игра завершается.

Пользователь может управлять персонажем за счёт нажатия стрелок или кнопок W, A, S, D. При нажатии пользователем одной из кнопок управления, программа проверяет, возможно ли передвинуть в указанном направлении персонажа, и, если это так, то делает это.
Программа проверяет, был ли собран ресурс (проверяя взаимное расположение по координатам) и, если это истинно, увеличивает счётчик собранных объектов. По достижении счётчиком возможного максимума игра завершается выигрышем пользователя.

Приложение должно предоставлять пользователю возможность наблюдать оставшееся время (в минутах и секундах), счёт и количество жизней.

После прохождения игры пользователю будет предложено начать игру заново.

## Сценарий использования программы:
1) 
 - Пользователь нажимает SPACE в начале игры -- программа запускается: начинается отсчёт таймера и передвижение "врагов", главный персонаж ставится в стартовую позицию (центр поля).
 
 - Пользователь нажимает SPACE в конце игры -- игра перезапускается и пользователю предоставляется возможность сыграть снова;

2)
 - Пользователь нажимает W ИЛИ стрелку вверх -- игра проверяет, не выходит ли персонаж за пределы игрового поля, и, если он не за границами, сдвигает персонажа вверх; игра проверяет по координатам, был ли собран ресурс, и, если это так, увеличивает счётчик собранных предметов; игра сравнивает счётчик с максимально возможным его значением - если они совпадают, игра завершается;
 

3) 
 - Пользователь нажимает A ИЛИ стрелку влево -- игра проверяет, не выходит ли персонаж за пределы игрового поля, и, если он не за границами, сдвигает персонажа влево; игра проверяет по координатам, был ли собран ресурс, и, если это так, увеличивает счётчик собранных предметов; игра сравнивает счётчик с максимально возможным его значением - если они совпадают, игра завершается;

4) 
 - Пользователь нажимает S ИЛИ стрелку вниз -- игра проверяет, не выходит ли персонаж за пределы игрового поля, и, если он не за границами, сдвигает персонажа вниз; игра проверяет по координатам, был ли собран ресурс, и, если это так, увеличивает счётчик собранных предметов; игра сравнивает счётчик с максимально возможным его значением - если они совпадают, игра завершается;

5) 
 - Пользователь нажимает D ИЛИ стрелку вправо -- игра проверяет, не выходит ли персонаж за пределы игрового поля, и, если он не за границами, сдвигает персонажа вправо; игра проверяет по координатам, был ли собран ресурс, и, если это так, увеличивает счётчик собранных предметов; игра сравнивает счётчик с максимально возможным его значением - если они совпадают, игра завершается.
 
 6) 
 - Пользователь сталкивается с вражеским персонажем -- главный герой перемещается в стартовую позицию, количество собранных предметов и прошедшее время остаются неизменными. Если в стартовой позиции находится враг, его положение изменяется. Количество жизней уменьшается на единицу. Если жизней не остаётся, игра завершается.
 
 7) 
 - Если пользователь выигрывает/проиграет, на экран выводится соответствующее сообщение. Игроку предлагается нажать SPACE для повторной игры. Также пользователь может закрыть игру, нажав кнопку "Закрыть". 

## Внутренняя структура приложения:

В реализации приложения использовались классы.  
Класс Game - класс, атрибуты которого содержат в себе информацию о главных действующих персонажах игры (управляемый пользователем герой и его "враги"), дополнительных объектах (ресурс, жизни), состояниях, различных константах, влияющих на игровой процесс. Класс Game определяется в модуле game.py, переменная-экземпляр создается в функции GameInit() того же модуля.  
Класс Resource - класс, атрибуты которого хранят изображение ресурса и его координаты. Класс Resource определяется в модуле add.py, переменная-экземпляр является атрибутом класса Game.  
Класс Life - класс, атрибуты которого хранят изображение жизни и её координаты. Класс Life определяется в модуле add.py, переменная-экземпляр является элементом атрибута-списка класса Game.  
Класс Environment - класс, атрибуты которого хранят выводимые на экран тексты, не являющиеся непосредственно игровыми объектами: время и счёт. Класс Environment определяется в модуле add.py, переменная-экземпляр является элементом атрибута-списка класса Game.  
Класс Main - класс, атрибуты которого хранят информацию о главном персонаже: изображение, координаты, сдвиг по осям в случае нажатия клавиши передвижения. Класс Main определяется в модуле character.py, экземпляр является атрибутом класса Game.  
Класс Enemy - класс, атрибуты которого хранят информацию о второстепенных персонажах ("вражеских"): изображение, координаты, направление движения. Класс Enemy определяется в модуле character.py, экземпляр является атрибутом класса Game.  
Класс Sprite - класс, атрибуты которого хранят информацию об изображениях: непосредственно поверхность, которая будет изображена на экране, его размеры. Класс Sprite определяется в модуле sprites.py, является атрибутом классов, определяющих игровые объекты.

### Подробнее о классе Game: 

**Атрибуты класса:**

- main: Main - главный игровой персонаж, управляемый пользователем; является экземпляром класса Main (определён в модуле _characters.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- res: Resource - ресурс, который нужно будет собирать в течение игры; является экземпляром класса Resource (определён в модуле _add.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- lives: list(Life) - список экземпляров объектов класса Life (определён в модуле _add.py_) - жизней; публичный атрибут, так как к нему часто идёт обращение извне.

- enemies: list(Enemy) - список экземпляров объектов класса Enemy (определён в модуле _characters.py_) - вражеских объектов; публичный атрибут, так как к нему часто идёт обращение извне.

- time: int - начальное время; имеет целочисленный тип и первоначально равно значению start_time, взятому из модуля _constants.py_; публичный атрибут, так как к нему часто идёт обращение извне.

- score: int - счёт игры; имеет целочисленный тип, изначально равен нулю и увеличивается на единицу каждый раз, когда игрок собирает ресурс; публичный атрибут, так как к нему часто идёт обращение извне.

- lives_count: int - количество оставшихся жизней; имеет целочисленный тип и изначально устанавливается значение, равное lives_count, взятое из модуля _constants.py_; публичный атрибут, так как к нему часто идёт обращение извне.

- state: int - состояние игры; имеет целочисленный тип и может быть равно одному из трёх значений:
                0 - стартовое положение
                1 - основной процесс
                2 - конец
публичный атрибут, так как к нему часто идёт обращение извне.

- result: int - атрибут, хранящий результат игры; при запуске игры равен 0, при поражении устанавливается в значение -1, при победе приравнивается к единице; публичный атрибут, так как к нему часто идёт обращение извне.


- screen: Surface - экран, на котором отрисовываются все объекты; отсутствует изначально и добавляется после создания игровой переменной в функции GameInit(); публичный атрибут, так как к нему часто идёт обращение извне.

- font: Font - устанавливает шрифт, используемый в игре, и его размер (которые, в свою очередь, описаны в модуле _constants.py_); отсутствует изначально и добавляется после создания игровой переменной в функции GameInit(); публичный атрибут, так как к нему часто идёт обращение извне.

- timer: Clock - атрибут, позволяющий в дальнейшем установить tick для задержки; отсутствует изначально и добавляется после создания игровой переменной в функции GameInit(); публичный атрибут, так как к нему часто идёт обращение извне.

- env:  Environment - атрибут, хранящий тексты, отображающиеся на экране во время игрового цикла; является экземпляром класса Environment (определён в модуле _add.py_); отсутствует изначально и добавляется в функции MainLoop модуля _game.py_; публичный атрибут, так как к нему часто идёт обращение извне.

- running: True - атрибут, хранящий информацию об исполнении игры

**Методы класса:**

- restart() - перемещает игрового персонажа в начальную позицию, генерирует заново списки врагов и жизней, устанавливает таймер в начальное время, обнуляет счёт, восстанавливает количество жизней и устанавливает атрибут, показывающий состояние, равным единице (т. к. требуется запустить основной игровой цикл); публичный метод, так как может быть вызван извне.

### Подробнее о классе Resource:

**Атрибуты класса:**

- img: Sprite - атрибут, хранящий изображение ресурса; является экземпляром класса Sprite (определён в модуле _sprites.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- x: int - координата x ресурса (рандомное число, находящееся в пределах экрана и не находящееся в координатах стартовой позиции игрока); имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

- y: int - координата y ресурса (рандомное число, находящееся в пределах экрана и не находящееся в координатах стартовой позиции игрока); имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

**Методы класса:**

- regen() - изменяет координаты x и y ресурса, опираясь на те же правила генерирования; вызывается в случае сбора ресурса; публичный метод, так как может быть вызван извне.

### Подробнее о классе Life:

**Атрибуты класса:**

- img: Sprite - атрибут, хранящий изображение ресурса; является экземпляром класса Sprite (определён в модуле _sprites.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- x: int - координата x ресурса; имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

- y: int - координата y ресурса; имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

**Методы класса:**

- destroy() - заменяет изображение на пустое (таким образом, визуально жизнь стирается с экрана); вызывается в случае столкновения с врагом; публичный метод, так как может быть вызван извне.

### Подробнее о классе Environment:

**Атрибуты класса:**

- time_text: Surface - время, отображаемое на экране; является поверхностью; отсутствует изначально и добавляется в функции MainLoop модуля _game.py_; публичный атрибут, так как к нему часто идёт обращение извне.

- score_text: Surface - счёт, отображаемый на экране; отсутствует изначально и добавляется в функции MainLoop модуля _game.py_; публичный атрибут, так как к нему часто идёт обращение извне.

**Методы класса: _у данного класса отсутствуют методы_**

### Подробнее о классе Main:

**Атрибуты класса:**

- img: Sprite - атрибут, хранящий изображение персонажа; является экземпляром класса Sprite (определён в модуле _sprites.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- x: int - координата x персонажа; имеет целочисленный тип, изначально устанавливается в середину экрана (константа из модуля _constants.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- y: int - координата y персонажа; имеет целочисленный тип, изначально устанавливается в середину экрана (константа из модуля _constants.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- vx: int - показывает скорость изменения движения по оси Оx; имеет целочисленный тип, изначально равен нулю, так как персонаж стоит в середине экрана и ждёт управления пользователем, изменяется в ходе игры; публичный атрибут, так как к нему часто идёт обращение извне.

- vy: int - показывает скорость изменения движения по оси Оy; имеет целочисленный тип, изначально равен нулю, так как персонаж стоит в середине экрана и ждёт управления пользователем, изменяется в ходе игры; публичный атрибут, так как к нему часто идёт обращение извне.

**Методы класса:**

- reset() - устанавливает персонажа в начальную позицию с сохранением текущих значений vx, vy; вызывается в случае столкновения с врагом; публичный метод, так как может быть вызван извне.

- regen() - устанавливает персонажа в начальную позицию, обнуляя при этом значения vx и vy; вызывается в случае перезапуска игры; публичный метод, так как может быть вызван извне.

### Подробнее о классе Enemy:

**Атрибуты класса:**

- img: Sprite - атрибут, хранящий изображение персонажа; является экземпляром класса Sprite (определён в модуле _sprites.py_); публичный атрибут, так как к нему часто идёт обращение извне.

- x: int - координата x объекта (рандомное число, находящееся в пределах экрана и не находящееся в координатах стартовой позиции игрока); имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

- y: int - координата y объекта (рандомное число, находящееся в пределах экрана и не находящееся в координатах стартовой позиции игрока); имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

- vx: int - показывает скорость изменения движения по оси Оx; имеет целочисленный тип, рандомное значение в пределах от 1 до максимальной скорости (константа из модуля _constants.py_), взятое в направлении оси Ох или в противоположном (определяется случайным образом), изменяется в ходе игры; публичный атрибут, так как к нему часто идёт обращение извне.

- vy: int - показывает скорость изменения движения по оси Oy; имеет целочисленный тип, рандомное значение в пределах от 1 до максимальной скорости (константа из модуля _constants.py_), взятое в направлении оси Оy или в противоположном (определяется случайным образом), изменяется в ходе игры; публичный атрибут, так как к нему часто идёт обращение извне.

**Методы класса:**

-regen() - проверяет текущую позицию экземпляра и, если она попадает в зону начального нахождения главного персонажа, изменяет её; вызывается в случае столкновения игрока с врагом (и, как следствие, помещения персонажа в стартовую позицию); публичный метод, так как может быть вызван извне.

### Подробнее о классе Sprite:

**Атрибуты класса:**

- name: str - наименование изображения; используется в тестировании; приватный атрибут.

- sprite: Surface - изображение, которое будет отрисовано на экране; является поверхностью; публичный атрибут, так как к нему часто идёт обращение извне.

- w: int - ширина изображения; имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

- h: int - высота изображения; имеет целочисленный тип; публичный атрибут, так как к нему часто идёт обращение извне.

**Методы класса: _у данного класса отсутствуют методы_**

## Реализация:

В ходе реализации программы не было обнаружено расхождений с функциональными и структурными моделями.

## Ссылки на графическое представление структурных моделей проекта:
- UML Activity Diagram (Character Movement): https://github.com/rensffz/project/blob/main/doc/UML%20AD%20Character%20Movement.pdf
- UML Activity Diagram (Show Result): https://github.com/rensffz/project/blob/main/doc/UML%20AD%20Show%20Result.pdf
- UML Activity Diagram (Start the Game): https://github.com/rensffz/project/blob/main/doc/UML%20AD%20Start%20the%20game.pdf
- State Machine Diagram: https://github.com/rensffz/project/blob/main/doc/State%20Machine%20Diagram.pdf
- Sequnece Diagram: https://github.com/rensffz/project/blob/main/doc/Sequence%20Diagram.pdf
- Class Diagram: https://github.com/rensffz/project/blob/main/doc/Class%20Diagram.pdf
- Component Diagram: https://github.com/rensffz/project/blob/main/doc/Component%20Diagram.pdf


