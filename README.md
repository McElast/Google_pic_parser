Google pictures Grabber (Парсер картинок Гугла)

--------------- English -------------------

Written in python 3.8.2

You need to install libraries: BeautifulSoup4, requests, selenium.

SETTINGS:

PATH – directory to save files
WORD – search query
N – numbers of pages to list (1 page = 100 pictures)
SIZE_BIG, SIZE_ANY, SIZE_MIDDLE – size of pictures to search. Change it in function pic_size_to_search. By default argument equals SIZE_BIG.


Then just run script.

While gathering links to pictures you’ll see right-click mouse button effect. Don’t get scared. This is needed to grab href from links (they are hidden until right click).

During working, you will see hints in console (how much grabbed, errors).

Thanks.

--------------- Русский -------------------

Написано на python 3.8.2

Для работы нужно установить: BeautifulSoup4, requests, selenium.

Все достаточно просто: сделайте только некоторые настройки:

PATH – путь к файлам для сохранения
WORD – поисковый запрос
N – количество страниц, которые собираетесь пролистывать по результатам поиска (на одной странице 100 фоток)
SIZE_BIG, SIZE_ANY, SIZE_MIDDLE – размер картинок, которые выдает поиск. Настраивается в функции pic_size_to_search. По умолчанию стоит SIZE_BIG.

Далее просто запустите скрипт.

По мере работы программы в консоли будут появляться информационные подсказки (сколько ссылок получено, какие ошибки, сохранен ли конкретный файл, сколько всего удалось собрать ссылок).

В самом начале, когда будет работать SELENIUM, будет нажата правая кнопка мыши (это надо для того, чтобы появились ссылки, которые по умолчанию скрыты и подгружаются JS), так что не пугайтесь.

Спасибо.

