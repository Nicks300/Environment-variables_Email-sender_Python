# Письмо заказывали?

## Аннотация

Данный проект позволит Тебе изучить, что такое аннотации типов, познакомит с понятиями - переменные окружения и конфиги,
ну и конечно научит отправлять письма на электронную почту.

## Содержание

1. [Chapter I](#chapter-i) \
    1.1. [Общая инструкция](#общая-инструкция) \
    1.2. [Введение](#введение)
2. [Chapter II](#chapter-ii) \
    2.1. [Статическая и динамическая типизация](#статическая-и-динамическая-типизация) \
    2.2. [Аннотации-типов](#аннотации-типов) \
    2.3. [Задание 1](#задание-1) \
    2.4. [Задание 2](#задание-2) \
    2.5. [Задание 3](#задание-3)
3. [Chapter III](#chapter-iii) \
    3.1. [Переменные окружения](#переменные-окружения) \
    3.2. [Конфигурационные файлы](#конфигурационные-файлы) \
    3.3. [Задание 4](#задание-4) \
    3.4. [Задание 5](#задание-5)
4. [Chapter IV](#chapter-iv) \
    4.1. [Отправка писем по почте](#отправка-писем-по-почте) \
    4.2. [Задание 6](#задание-6) \
    4.3. [Задание 7](#задание-7) 
5. [Chapter V](#chapter-v) \
    5.1. [Задание 8](#задание-8)  \
    5.2. [Задание 9](#задание-9) 

## Chapter I

### Общая инструкция

Привет, студент! \
Рады приветствовать тебя на нашем интенсиве по языку Python. \
Перед тем как начать, хочется сказать тебе несколько напутствий:
1. Наша команда - не медики. Если ты будешь видеть в тексте медицинские неточности или ошибки, заранее просим у тебя прощения. Оставляй нам обратную связь и мы все поправим!
2. Повествование ведется иногда немного в шутливой форме, чтобы не быть скучным. Однако, как ты и сам знаешь, юмор и шутки - это субъективная вещь. Поэтому, если каламбуры в данном тексте по твоему мнению попахивают батиным юмором, то, пожалуйста, просто прими это.
3. Не забывай, что отсутствие подробной теории и примеров - это не баг, а фича, как любят говорить разработчики. Не забывай, что Google, а теперь уже и ChatGPT - это верные помощники программиста!
4. Упоминая ChatGPT, хочется отметить, что на данном этапе он может часто ошибаться. Полагайся больше на себя!
5. Если ты на чем-то застрял и кажется, что уже все перепробовал и не знаешь куда идти - передохни! Поверь, этот совет помогал многим разработчикам в их работе. Проветрись, перезагрузи голову и, возможно, в следующий раз тебе в голову придет нужное решение!
6. **Жирным** шрифтом будут выделены слова на которые тебе нужно будет обратить более пристальное внимание, не стесняйся их гуглить!
7. *Курсивом* будут выделены имена папок и файлов, названия проектов и т.д.
8. В такой блок `<вставь сюда данные>` нужно подставить что-то из твоего кода, возможно какую-то переменную.
9. Перед выполнением проекта необходимо склонировать с GitLab одноименный репозиторий.
10. Все файлы с кодом необходимо создавать в папке *src/* склонированного репозитория.
11. Каждое задание необходимо выполнять в отдельном файле. Название должно содержать *task_* и номер задания. Пример, *task_1.py*, *task_2.py* и т.д. 
Если задание подразумевает создание дополнительных файлов, то их местоположение в папке *src* и названия будут прописаны в теле задания.

Удачи тебе в этом тернистом, но определенно полезном пути!

### Введение

Новый день - новые возможности, думаешь ты входя в, уже такую привычную тебе, поликлинику. Ты заходишь в кабинет и видишь глав-врача,
стоящего рядом с уже знакомыми тебе двумя стажерами из других поликлиник. Ты издаешь очень тяжелый и протяжный стон.

> О, какие люди в Голливуде! Да еще и без охраны.
>> Глав-врач

> Опять эти присказки...
>> Стажер, думает про себя, стараясь не закатить глаза

> Ничего, ничего, вырастите потом, посмотрим, как ваши дети и внуки будут реагировать на ваши нормисы и дед инсайды.
> 
> Ладно, как ты видишь к нам снова пожаловали Вупсень и Пупсень. Так что сегодня, ты, Лунтик, будешь работать вместе с ними.
> И задачка как раз у меня для вас есть. У нас тут пациенты стали жаловаться, что им видите ли непонятен наш почерк в рецептах.
> Ни им, ни аптекарям, ни местному кружку шифровальщиков-любителей. Хотелось бы им ответить, что мы им не мастера каллиграфии,
> но как вы знаете, людям хамить - плохо, а делать их жизнь лучше - хорошо. Вернемся к сути. Задача следующая - дать возможность
> нашим врачам вбивать назначаемые рецепты электронно с двумя опциями:
> 1. Сохранять рецепт в файл, чтобы потом его печатать клиенту.
> 2. Отправлять рецепт по электронной почте.
>
> Ну что, три товарища, трижды подумайте над задачей и сообразите ее на троих. И скажите, спасибо, что я ограничился всего тремя крылатыми фразами про троих.
>> Глав-врач

## Chapter II

### Статическая и динамическая типизация

> Перед тем, как приступить к основной задаче, вам бы надо изучить, что такое **аннотации типов**.
> 
> Скажу буквально пару слов про них. Языки программирования можно разделить на две группы - со **статической** и с **динамической**
> **типизациями**. Что это означает? Легче показать на примерах. Вот часть кода из языка C с присваиванием переменной:
> ```
> int a;  // Объявление переменной a
> a = 10; // Присвоение значения переменной a
> ```
> Как вы видите, в коде сразу обозначается, что переменная `a` имеет целочисленный тип данных. Если вы попробуйте переприсвоить
> этой переменной значение из другого типа:
> ```
> int a;  // Объявление переменной a
> a = 10; // Присвоение значения переменной a
> a = 'some_str'; // Присвоение значения другого типа переменной a
> ```
> то программа выдаст ошибку. В переменную `a` могут быть записаны только целые числа - это было объявлено ранее. 
> И не только в обычных переменных. Тип каждого аргумента функции, что возвращает функция и т.д. - сразу устанавливается в коде.
> Если очень просто, то это и есть **статическая типизация**. 
> 
> Python - это язык с **динамической типизацией** (подробнее почитайте сами) - это удобнее для более быстрого программирования, более гибкого, идеально для прототипирования.
> Однако, не зря огромное число популярных языков имеет **статическую** типизацию. Это защищает от многих ошибок, от неожиданных поведений.
> Вы строго обозначаете сразу те условия, которым должна следовать ваша программа и все переменные в них. **Статическая типизация** - это порядок, за который надо платить
> громоздкостью и некоторым неудобством при написании кода. **Динамическая** же **типизация** - это управляемый хаос, который позволяет достигнуть ваших целей (написать нужный код) гораздо быстрее.
> Но хаос есть хаос, где-то может выстрелить что-то, что вы не продумали изначально.
>> Глав-врач

### Аннотации типов

> Поэтому с какого-то момента в Python этот хаос попытались сделать еще чуть более упорядоченным и ввели **аннотации типов**.
> Они не обязательны и служат лишь дополнительным инструментом. Однако, уже на текущий момент, их использование является негласным обязательным правилом
> для написания любого продакшн Python кода.
> 
> Я подготовил вам 6 задач, по две на брата (или сестру), при написании которых необходимо расставить все аннотации типов, используя
> встроенную библиотеку `typing`.  При этом, если в задании указано какой тип данных находится в коллекции - это должно быть указано в аннотации. Если число элементов в коллекции определено заданием, то должны быть проставлены
> типы для каждого элемента. Для всех коллекционных типов (список, кортеж, словарь и т.д.) для аннотации используйте только библиотеку `typing`, а не встроенные типы.
> 
> Не забудьте, что вы можете делать задания параллельно в разных ветках, а потом уже объединить их в одной.
> 
> **ОБЯЗАТЕЛЬНОЕ УСЛОВИЕ ДЛЯ ВСЕХ ЗАДАЧ В ЭТОМ ПРОЕКТЕ**. Если вы где-то используйте условную конструкцию `if-elif-else`, и внутри блоков
> происходит операция с разными типами (например, по условию в один блок попадает число, а в другой строка, при этом и там, и там происходит операция умножения), то в условие необходимо добавить проверку на тип. Ведь умножение для чисел
> и умножение для строк - две большие разницы! Пример:
> ```python
> from typing import Union, Optional
> 
> 
> def func(a: str, b: Union[str, int]) -> Optional[Union[str, int]]:
>   if a == 'integer' and isinstance(b, str):
>       return b * 2
>   elif b == 'string' and isinstance(b, int):
>       return b * 2
>   else:
>       return None
> ```
> Данное условие будет строго проверяться тестами.
> 
> Если аргумент функции или метода класса, или того, что они возвращают, является объектом какого-то класса, то необходимо указывать этот класс в аннотации. Пример:
> ```python
> class Example:
>   ...
> 
> object_example = Example()
> 
> def func(example: Example) -> None:
>   print(type(example))
> 
> func(object_example)
> ```
> 
> Класс может быть не только созданным вручную, но и импортированным из библиотеки, не забывайте это!
>> Глав-врач

### Задание 1

> Первая пара задач:
> 1. Напишите функцию `process_numbers`, которая принимает один аргумент - список, состоящий только из целых чисел.
> Внутри функции нужно найти - минимум, максимум и среднее, округленное до одного знака после запятой, в этом списке.
> И вернуть их в виде кортежа в порядке, перечисленном ранее.
> 2. Напишите функцию `find_item`, которая принимает два аргумента:
>    1) словарь, ключи которого всегда строки, а значения - целые числа;
>    2) строку.
>    
>   Функция должна проверять, есть ли переданная строка (второй аргумент) в ключах словаря. Если есть, то функция должна возвращать значение по этому ключу, 
> если нет, то возвращать `None`.
>  
>> Глав-врач

Кажется тут все понятно, главное не забыть, что обе функции нужно реализовать в файле *src/task_1.py*.

### Задание 2

> Вторая пара задач:
> 1. Напишите функцию `number_of_differences`, которая принимает два аргумента. Оба аргумента - списки, которые могут содержать
> элементы следующих типов данных - целые числа, строки, булевый тип.
> 
>   Функция должна возвращать кол-во элементов, которые есть во втором списке (2 аргумент), но которых нет в первом списке (1 аргумент).
> При этом подсчет нужно вести только по элементам, ранее озвученных, трех типов - целые числа, строки, булевый тип.
> 2. Напишите функцию `calculate_area`, которая принимает два аргумента:
>    1) строку;
>    2) или кортеж с двумя числами с плавающей точкой, или одно число с плавающей точкой.
>    
>   Функция должна считать и возвращать площадь геометрической фигуры, округленную до 2 знаков после запятой. 
> Первый аргумент-строка отвечает за название фигуры. Второй аргумент отвечает за размеры, которые
> требуются для расчета площади. Если:
>   - первый аргумент равен `rectangle`, то функция должна вычислить площадь прямоугольника. Соответственно во второй аргумент
> будет передаваться кортеж с шириной и длиной фигуры;
>   - первый аргумент равен `circle`, то функция должна вычислить площадь круга. Соответственно во второй аргумент будет передаваться
> радиус круга. Формула площади круга равна `S = pi * r * r`, где `pi = 3.14159`;
>   - первый аргумент равен любой другой строке, то функция должна возвращать `None`.
>3. Не забудь строго проверять типы аргументов, переданных функции. Если они не равны тому, что объявлено в задании, то пусть функция возвращает `None`.
>> Глав-врач

И тут тоже все понятно. Обе функции нужно реализовать в файле *src/task_2.py*. \

### Задание 3

> Третья пара задач:
> 1. Напишите функцию `comparison_dict_and_list`, которая принимает два аргумента:
>   1) словарь, ключи и значения которого являются строками;
>   2) список строк.
> 
>   Функция должна проверять, встречается ли хоть один элемент из списка (2 аргумент) в значениях словаря (1 аргумент).
> Если хоть один элемент встречается, то функция должна возвращать булево значение `True`, если нет, то булево значение `False`.
> 2. Напишите функцию `get_user_info`, которая принимает два аргумента:
>   1) список словарей, в каждом словаре все ключи - это строки, а значения могут иметь абсолютно любой тип;
>   2) строку.
>   
>   Каждый словарь из списка (1 аргумент), содержит информацию о человеке. Пример 1 аргумента:
>   ```python
>   user_list = [
>        {'name': 'Ivan', 'age': 15, 'weight': 49.5, 'has_wife': False},
>        {'name': 'Petr', 'age': 35, 'weight': 80.1, 'has_wife': True},
>   ]
>   ```
>   Во 2 аргументе передается имя человек (`Ivan` или `Petr`). Функция должна проверить, есть ли в списке словарь с человеком с таким именем.
> Если такой человек обнаружен, то функция должна вернуть словарь с его данными. Если такого человека нет, то необходимо вернуть `None`.
>> Глав-врач

Обе функции нужно реализовать в файле *src/task_3.py*.

### Chapter III

### Переменные окружения

> Перед тем, как перейти уже к реализации задачи, давайте я вам расскажу о тех вещах, которые активно используются в реальных
> проектах на пайтон - это переменные окружения и конфиги.
> 
> Давайте начнем с переменных окружения. Представьте, что у вас есть переменные, которые активно используются в коде. Как пример,
> переменные - логин и путь к папке, откуда читаются и куда сохраняются файлы. Допустим эти переменные часто используются.
> Как мы их обычно задаем? Либо в самом коде, либо вводя с клавиатуры. То есть если мы хотим поменять значение этой переменной, то
> нам надо либо лезть в код, либо все важные переменные при запуске вводить с клавиатуры. Это далеко всегда не удобно.
> Тут и появляются переменные окружения.
> 
> Переменные окружения - это глобальные переменные, которые можно задавать в отдельном файле (на самом деле не только).
> В дальнейшем эти переменные подгружаются в код и используются. Файл, в который обычно записываются переменные окружения
> называется `.env`. И да - это все название файла, ничего дописывать не нужно. Пример того, как выглядит `.env` файл:
> ```
> LOGIN=krushitel2012
> HOME_PATH=/home/user/
> ```
> Сами переменные обычно пишутся в верхнем регистре. Для значений (даже если они строки), никаких кавычек не нужно.
> 
> Фактически в файл `.env` выносятся все переменные, которые конфигурируют проект и могут меняться в дальнейшем. Очень удобно
> хранить их и менять в одном месте.
>> Глав-врач

### Конфигурационные файлы
 
> Теперь перейдем ко второму пункту - конфигурационные файлы или конфиги. Переменные окружения - это лишь переменные и 
> значения этих переменных. Их нужно каким-то образом грамотно подгрузить в код и удобно оформить. Для этого служат конфиги. Что такое конфиг?
> Это оформление всех настроек проекта (включая все важные переменные) в один файл (в нашем случае, в питон файл).
> Конфиги нам позволяют отделить настройки проекта (какие-то важные глобальные переменные) от самого кода, что повышает читабельность, гибкость и безопасность
> Часто конфиги описываются отдельными классами, в которых хранятся атрибуты классов, содержащие уже конкретные переменные со значениями.
> 
> Итак, как я уже сказал, конфиги оформляются обычно в виде классов в отдельных файлах с названиями типа - `config.py` или `settings.py`:
> ```python
> class Configuration:
>   login: str
>   base_folder: str
> ```
> Данная запись новая для вас. Она показывает, что класс `Configuration` должен содержать 2 атрибута, но это лишь пожелание.
> Чтобы там были значения, нужно либо их задать явно, либо использовать метод `__init__`.
> Как я уже сказал ранее, по хорошему теперь нужно каким-то образом передать переменные окружения (записанные в `.env`) в эти атрибуты класса.
> 
> А вот это уже вы выясните сами. Способов на самом деле много, я бы посоветовал сделать это с помощью библиотеки `python-dotenv` и
> классом `BaseSettings` из библиотеки `pydantic_settings`. Главное разберитесь, как это сделать без метода `__init__`.
> 
> И еще, обратите внимание на аннотации у переменных класса. В конфиге они строго обязательны.
>> Глав-врач

### Задание 4

> Итак, я подготовил для вас в [следующей папке](materials/doctors) пару json файлов с описанием характеристик конкретных врачей.
> Название файлов - это их логины. Ваша задача создать файл с двумя переменными окружения - `login` и `base_folder`, в которых
> могут записываться логин врача, карточку которого вы хотите прочитать и папку внутри проекта, где лежит папка `doctors/`.
> В данном случае - это папка `materials`. Знак `/` в переменной окружения `base_folder` в конце названия папки ставить не надо!
> 
> После этого нужно написать конфиг файл с классом `Configuration` с двумя атрибутами `login` и `base_folder`. Данный класс
> должен будет автоматически подгружать в свои атрибуты соответствующие переменные окружения.
> 
> И последнее, нужно создать основную функцию, где будет инициализироваться объект класса `Configuration`, а дальше с помощью
> атрибутов объекта этого класса, считываться в словарь карточка того врача чей логин указан в переменной окружения. Пусть
> функция возвращает этот словарь.
> 
> Не используйте внутри основной функции явной прописанные логин и основную папку. Используйте вместо этого параметры конфига - 
> `login` и `base_folder`.
>> Глав-врач

Кажется тут уже требуется некоторая небольшая структуризация услышанного. Что же получается:
1. В файле `src/.env` необходимо прописать две переменные окружения `login` и `base_folder`. Не забыть про верхний регистр для переменных окружения.
В переменной `base_folder` должен лежать путь к папке, где лежит папка `doctors/` относительно рабочей папки (папки с проектом).
По-умолчанию, эта папка лежит в папке `materials`. Если бы она лежала в папке `materials/examples`, то соответствующее значение
должно было бы лежать в переменной. В переменной `login` должен лежать логин врача (совпадающий с названием файла с его карточкой без расширения файла).
2. В файле `src/config_4.py` создать класс `Configuration` с двумя атрибутами `login` и `base_folder`, указав их аннотации.
3. В этом же файле `src/config_4.py` написать код, который позволит автоматически подгружать переменные окружения при создании
объекта класса `Configuration` в соответствующие переменные.
4. В файле *src/task_4.py* необходимо реализовать функцию `main`, в которой прописать всю основную логику.
5. Вызов функции `main` осуществить в блоке `if __name__ == "__main__":`.
6. В функции `main` (не принимает никаких аргументов) необходимо создать экземпляр класса `Configuration` и далее использовав его атрибуты, прочитать файл
с карточкой врача и записать содержимое в словарь. Функция `main` должна ВОЗВРАЩАТЬ этот словарь (а НЕ выводить его на экран).
7. Проставьте везде аннотации, если их можно проставить (включая функцию `main`). Тесты это будут проверять!

P.S. Не забудьте назначить рабочую папку в PyCharm, как папку с проектом. А все пути для файлов и импортов писать относительно 
этой рабочей папки.

### Задание 5

> Ну что ж, теперь можно потихоньку переходить к сути. Давай начнем с того, что дадим врачу возможность выписывать рецепт электронно.
> Я знаю, что ты уже что-то подобное делал в прошлых проектах. Если я не ошибаюсь, ранее ты давал возможность вести прием
> врачу электронно (по-моему даже в таком же групповом проекте). Сейчас я хочу похожего, только с тремя особенностями:
> 1. Реализовать все через класс.
> 2. Дать выбор врачу записывать его рецепт в файл или нет. Если он хочет записать в файл, то пусть указывает название файла.
> 3. Перед запуском программы врач вводит свой логин и путь до папки *doctors/* в файл с переменными окружения, программа читает его карточку, а в конце любого рецепта добавляет к нему на разных строках
> ФИО врача и его специальность (прочитанные из карточки). Чтобы выглядело, как подпись.
> 
> Твоя же главная функция `main` должна возвращать записанный с клавиатуры рецепт в виде строки.
>> Глав-врач

Тут уж точно не обойтись без переформулирования ТЗ в более четкой форме, а именно:
1. В файле *src/doctor_5.py* создать класс `Doctor`. В этом классе создать:
    - метод `__init__`, который принимает один аргумент - объект класса `Configuration` и внутри определяет 3 атрибута обьектов - `config`, `name` и `speciality`.
В атрибут `config` должен записываться передаваемый в метод конфиг. С помощью него в `__init__` должна читаться карточка врача из нужного файла (логин определен в конфиге).
В атрибут `name` должно записываться ФИО через пробел (как оно записано в карточке), в атрибут `speciality` - специальность врача из карточки (как она указана там).
    - приватный метод объекта `__write_receipt_to_file`, который принимает на вход два аргумента - рецепт и имя файла (БЕЗ РАСШИРЕНИЯ). Метод должен записывать
рецепт в текстовый файл с переданным в метод названием (добавляя расширение *.txt*) в папку *receipts/*, которая должна лежать в той же папке, что и папка *doctors/*. Т.е. для пути нужно использовать
единую папку, указанную в конфиге;
    - метод объекта `write_recipe`, который принимает на вход один аргумент - имя файла, в который надо записать рецепт (БЕЗ РАСШИРЕНИЯ). По-умолчанию значение аргумента `None`.
Метод должен выводить на экран приглашение ко вводу `Введите рецепт (чтобы закончить введите два раза пустую строку): `,
а далее давать возможность многострочного ввода, с возможностью переноса строки и пропуска одной строки.
При этом, если он пропустил 2 строки подряд, то ввод должен прекращаться. Пример (слева проставлена нумерация строк, она не вводится, нужна чтобы отследить пустые строки):
        ```
        1 Введите записи (чтобы закончить нажмите два раза Enter):
        2 Ввожу данные
        3 
        4 Такие данные
        5 
        6 Сякие данные
        7
        8
        ```
        После этого нужно удалить из введенного рецепта последний пропуск строки и вставить на разных строках ФИО и специальность врача,
добавив перед ней слово `Врач-`. Пример:
        ```
        1 Ввожу данные
        2 
        3 Такие данные
        4 
        5 Сякие данные
        6
        7 Иванов Иван Иванович
        8 Врач-Терапевт
        ```
      Если в функцию было передано имя файла, то в ней нужно вызвать приватный метод `__write_receipt_to_file` и записать рецепт в файл.
Если же осталось значение по-умолчанию, то записывать рецепт не нужно. Метод ВСЕГДА должен возвращать введенный 
отредактированный рецепт в виде строки.
3. В файле *src/task_5.py* необходимо реализовать функцию `main`, в которой прописать всю основную логику.
4. Вызов функции `main` осуществить в блоке `if __name__ == "__main__":`.
5. В функции `main` необходимо создать экземпляр конфига и экземпляр класса `Doctor`. Далее дать возможность врачу ввести с клавиатуры ответ на вопрос - 
нужно ли сохранять файл?
    ```
    Нужно ли будет сохранить рецепт в файле? 
    ```
   Если врач ввел любой символ (а не просто сразу нажал Enter), то далее нужно дать ему возможность ввести имя файла:
    ```
    Введите имя файла, куда будет сохранен рецепт: 
    ```
   Далее нужно получить рецепт с помощью метода `write_recipe`, передав или не передавая имя файла, в зависимости от ответов пользователя.
6. Функция `main` (не принимает никаких аргументов) должна возвращать рецепт, полученный с помощью метода `write_recipe`.
7. Проставить везде аннотации, если их можно проставить (включая функцию `main` и все методы класса). Тесты это будут проверять!

P.S. Не забудьте назначить рабочую папку в PyCharm, как папку с проектом. А все пути для файлов и импортов писать относительно 
этой рабочей папки.

## Chapter IV

### Отправка писем по почте

> Вы еще не забыли к чему весь этот сыр-бор? А я вам напомню! Нам нужно отсылать рецепты врачей пациентам на почту.
> 
> Пришло время немного научиться работать через код с почтой. Но для начала нужно в целом понять, как работает почта. Когда вы отправляете
> письмо со своего браузера или приложения, оно уходит на сервер исходящей почты (если у вас почта на яндексе, то на сервера яндекса).
> Оттуда это письмо отправляется на сервер входящей почты (допустим вы шлете сообщение на gmail почту, тогда сервер будет гугловский).
> А дальше уже тот, кому вы шлете это сообщение, подгружает это сообщение себе в приложение с сервера (это конечно делается все за кадром автоматически).
> 
> Так вот отправка на сервер вашей почты с вашего клиента и между серверами осуществляется через протокол **SMTP**. Протокол 
> в сетях - это набор правил по которым общаются между собой компьютеры в сети. А к чему это я? А к тому, что с помощью **SMTP**,
> вы и будете слать сообщения пациенту через код. Используй для этого библиотеку `smtplib`.
> 
> Как упрощенно выглядит путь электронного письма в сети - разобрались. Теперь давайте пару слов о том, что вообще представляет
> собой письмо, которое шлется по **SMTP**. Вы должны понимать, что электронное письмо - это не просто текст в теле письма.
> Это еще и разные полезные поля (почта адресата, тема письма, копии и т.д.), а также возможность прикреплять файлы к письму - 
> картинки, пдфки и т.д. Чтобы это все это дошло в том виде, который вы задумали, отправляя письмо (вначале текст, дальше картинка с подписью,
> а внизу прикрепленный архив со смешными мемами) существует стандарт **MIME multipart**. Этот стандарт позволяет включать
> в одно сообщение части с разными типами и сохранять их порядок и нужную структуру. С помощью этого стандарта вы и будете формировать тело письма, определять кому отправляете,
> тему и т.д. А уже сформированный **MIME multipart** и будет отсылаться по **SMTP**. Используй для формирования **MIME multipart**
> библиотеку `email`. Для тела письма используй **MIME text**.
> 
> Суть я вам объяснил, а уже детали вы гугланете сами.
>> Глав-врач

### Задание 6

> Итак, в первую очередь создайте временную почту в яндексе, с которой будете слать сообщения. Новая почта нужна, так как для
> отправки письма придется вводить пароль к ней. После вашей стажировки вы ее всегда сможете удалить. Главное не используйте личную почту!!! 
> Мы ценим ваши персональные данные и не хотим их знать.
> 
> Далее необходимо добавить новые переменные окружения:
> - SMTP_SERVER - SMTP сервер, для яндекса - это `smtp.yandex.ru`;
> - SMTP_PORT - порт данного сервера, для яндекса - это `587`;
> - SMTP_EMAIL - полный адрес почты, которую вы создали;
> - SMTP_EMAIL_PASSWORD - пароль к этой почте.
> 
> Для данных переменных создайте отдельный конфигурационный класс, куда будут подгружаться все переменные окружения с префиксом `smtp_` и
> записывать в атрибуты без этого префикса (т.е. атрибуты класса будут - `server`, `port`, `email` и `email_password`). 
> Для этого можно использовать `SettingsConfigDict` из `pydantic_settings`. 
> 
> Ну и что касается почты. Давай начнем с того, чтобы создать класс для формирования MIME multipart. Не забудь дать возможность
> врачу вводить почту пациента с клавиатуры.
>> Глав-врач

Кажется, здесь требуется некая структуризация. Если подумать, то нужно сделать следующее:
1. В файле *src/.env* необходимо добавить 4 переменные окружения `SMTP_SERVER`, `SMTP_PORT`, `SMTP_EMAIL` и `SMTP_EMAIL_PASSWORD`.
Что в них прописать понятно из речи глав-врача.
2. В файл *src/config_6.py* добавить весь код из `src/config_4.py` + создать конфигурационный класс `SMTPSettings` с четырьмя атрибутами - `server`, `port`, `email` и `email_password` (они без префикса `smtp`!!!).
Класс должен забирать все переменные окружения с префиксом `smtp_`.
3. В файле *src/email_6.py* создать класс `EmailMessage`. В этом классе создать:
    - метод `__init__`, который принимает четыре аргумента - `from_email`, `to_email`, `subject` и `body` и записывает их в
одноименные атрибуты объекта. Данные атрибуты отвечают за: почту с которой посылается письмо (которую вы создали), почту кому вы посылаете,
тему и тело письма соответственно;
    - метод объекта `create_mime_message`, который не принимает аргументов. Внутри метода с помощью атрибутов объекта формируется
 объект класса `MIMEMultipart`, куда вставляются данные от кого письмо, кому письмо, тема письма и тело письма. Метод должен возвращать объект
MIME multipart.
4. В файле *src/task_6.py* необходимо реализовать функцию `main`, в которой прописать всю основную логику.
5. Вызов функции `main` осуществить в блоке `if __name__ == "__main__":`.
6. Функция `main` (не принимает никаких аргументов) должна запрашивать почту пациента с клавиатуры `'Введите почту пациента: '`. Функция должна возвращать 
сформированный MIME multipart со всеми обговоренными выше данными. Тему письма можно захардкодить, как `'Receipt'`, а в теле письма
всегда писать `'Test'.` Все остальные операции нужно сделать с помощью написанных ранее классов.
7. Проставить везде аннотации, если их можно проставить (включая функцию `main` и все методы класса). Тесты это будут проверять!

### Задание 7

> Дошли наконец до самого интересного. А именно - пора писать класс, который будет принимать **MIME multipart** и с помощью
> **SMTP** отправлять его на почту пациента. Дерзайте!
>> Глав-врач

Агась, тогда имеем следующее:
1. В файл *src/email_7.py* добавить весь код из *src/email_6.py* + создать класс `EmailSender`. В этом классе создать:
    - метод `__init__`, который принимает один аргумент `smtp_settings` и записывает его в соответствующий атрибут объекта. В этом атрибуте
должен храниться объект соответствующего конфигурационного файла с настройками SMTP;
    - метод объекта `send_email`, который принимает один аргумент - объект класса `EmailMessage` и записывает его в соответствующий атрибут объекта.
Получение MIME multipart нужно перенести внутрь данного метода. Метод должен с помощью SMTP настроек посылать по SMTP сформированный
MIME multipart. Если письмо отправилось успешно, необходимо выводить на экран фразу - `Письмо успешно отправлено`. При возникновении
любого исключения необходимо выводить на экран фразу - `Ошибка при отправке письма!`.
2. В файле *src/task_6.py* необходимо реализовать функцию `main`, в которой прописать всю основную логику.
3. Вызов функции `main` осуществить в блоке `if __name__ == "__main__":`.
4. Функция `main` (не принимает никаких аргументов) должна также запрашивать почту пациента с клавиатуры `'Введите почту пациента: '`. Функция должна отправлять письмо по введенному адресу.
Тему письма оставить захардкоженной, как `'Receipt'`, а в теле письма всегда писать `'Test'.` Все остальные операции нужно сделать с помощью написанных ранее классов.
Функция не должна ничего возвращать.
5. Проставить везде аннотации, если их можно проставить (включая функцию `main` и все методы класса). Тесты это будут проверять!

P.S. Проверьте работу программы, отправив письма на свои личные почты.

## Chapter V

### Задание 8

> Остался последний штрих! Теперь необходимо собрать все свои наработки из задания 4 и задания 7 в одну программу.
>> Глав-врач

1. Если работа была в разных ветках гитлаба, то необходимо смерджить ветки со всеми наработками в master и уже в нем дописать это задание.
2. Для основного кода надо использовать код из файлов *src/.env*, *src/config_6.py*, *src/doctor_5.py* и *src/email_7.py*.
3. В файле *src/task_8.py* необходимо реализовать функцию `main`, в которой прописать всю основную логику.
4. Вызов функции `main` осуществить в блоке `if __name__ == "__main__":`.
5. Функция `main` (не принимает никаких аргументов) должна дать возможность врачу ввести с клавиатуры ответ на вопрос - 
нужно ли сохранять файл?
    ```
    Нужно ли будет сохранить рецепт в файле? 
    ```
   Если врач ввел любой символ (а не просто сразу нажал Enter), то далее нужно дать ему возможность ввести имя файла:
    ```
    Введите имя файла, куда будет сохранен рецепт: 
    ```
   Далее нужно получить рецепт, передав или не передавая имя файла, в зависимости от ответов пользователя.\
   Далее нужно запросить почту пациента с клавиатуры `'Введите почту пациента: '`. \
   После этого необходимо отправлять рецепт на введенную врачом почту. Тему письма всегда указывать - `Рецепт`! Нужно обратить
внимание, что тут тема написана русскими буквами.

    Функция `main` не должна ничего возвращать.
6. Проставить аннотации в функции `main`. Тесты это будут проверять!

P.S. Обязательно проверьте, отправляя, введенный с клавиатуры рецепт, на свои личные почты.

### Задание 9

> Ну что, три товарища, примите мои поздравления! Правильно учили нас "Зачарованные", что "Сила трёх" - это сильнейшая магия
> этого мира! Ладно, не забудьте все запушить в GitLab. Только в этот раз есть один момент, как я уже говорил нас не интересуют
> ваши персональные данные (даже от новой почты), так что файл с переменными окружения не пуште. И надеюсь, что вы не использовали
> личную почту!
>> Глав-врач

Все что вам остается на сегодня - это **запушить** все наработки в **GitLab** (все файлы *.py*), включая файл *src/.env*

💡 [Нажми тут](https://forms.gle/eQ9oiDbhdv2BzjNT7), чтобы поделиться с нами обратной связью на этот проект в рамках тестирования. Это поможет команде Продукта сделать обучение лучше. Спасибо за участие!
