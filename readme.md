Тест-кейсы:

Допущения:
1. в примерах тест-кейсов не прикладываются скриншоты к ожидаемому результату
2. в ожиданиях не указываются атрибуты, что-бы не вводить в заблуждения (нет постановки)

***

Проверка перехода на экран с часами и применением группировки по типу товара:

1. Открыть главный экран -> https://opm-website.iot-asm-test1.insitech.live/
2. Нажать в подвале на блок с изображением Часов
3. Выполняется редирект на страницу с часами

*Результат* выполнен переход на экран с выбранной вкладкой "Часы".

*Ожидание* будет выполнен переход на экран с группировкой и отображением продукции только для "Часов"

*Баг* не применяется группировка, отображаются все данные по товарам в таблице ниже

*** 

Проверка возможности выбрать и перейти на карточку продукта из таблицы

1. Перейти на экран списка товаров -> https://opm-website.iot-asm-test1.insitech.live/constructor
2. Перейти на вкладку Часы
3. Выбрать производителя Lenovo
4. Выбрать модель S2

*Результат* выполнен переход на экран формирования заказа
*Ожидание*  будет выполнен переход на экран формирования заказа 

***

Проверка возможности найти через поиск продукт

1. Перейти на главный экран -> https://opm-website.iot-asm-test1.insitech.live/
2. В поле поиска ввести Lenovo s2

*Результат* товар найден
*Ожидание* товар будет найден  

***

Проверка возможности перейти на карточку товара найденного через поиск

1. Выполнить шаги кейса 3
2. Нажать на результат выдачи Lenovo s2
3. Будет выполнен переход на карточку продукта

*Результат* выполнен переход на карточку продукта
*Ожидание* будет выполнен переход на карточку продукта  

***

