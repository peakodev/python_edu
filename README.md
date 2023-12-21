# Python EDU GoIT

## Homework 6 (Робота з файлами)

У багатьох на робочому столі є папка, яка називається якось ніби "Розібрати". Як правило, розібрати цю папку руки ніколи так і не доходять.

Ми з вами напишемо скрипт, який розбере цю папку. Зрештою, ви зможете настроїти цю програму під себе, і вона виконуватиме індивідуальний сценарій, що відповідає вашим потребам. Для цього наш додаток буде перевіряти розширення файлу (останні символи в імені файлу, як правило, після крапки) і, залежно від розширення, приймати рішення, до якої категорії віднести цей файл.

Скрипт приймає один аргумент при запуску — це ім'я папки, в якій він буде проводити сортування. Допустимо, файл з програмою називається sort.py, тоді, щоб відсортувати папку /user/Desktop/Мотлох, треба запустити скрипт командою python sort.py /user/Desktop/Мотлох

Для того, щоб успішно впоратися з цим завданням, ви повинні винести логіку обробки папки в окрему функцію.
Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.
Скрипт повинен проходити по вказаній під час виклику папці та сортувати всі файли по групах:

 - зображення ('JPEG', 'PNG', 'JPG', 'SVG');
 - відеофайли ('AVI', 'MP4', 'MOV', 'MKV');
 - документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
 - музика ('MP3', 'OGG', 'WAV', 'AMR');
 - архіви ('ZIP', 'GZ', 'TAR');
 - невідомі розширення.

Ви можете розширити та доповнити цей список, якщо хочете.

Після необхідно додати функції, які будуть відповідати за обробку кожного типу файлів.

Крім того, всі файли треба перейменувати, видаливши із назви всі символи, що призводять до проблем. Для цього треба застосувати до імен файлів функцію normalize. Слід розуміти, що перейменувати файли треба так, щоб не змінити розширень файлів, регістр букв розширень теж не можна змінювати.

### Функція normalize:

Проводить транслітерацію кириличного алфавіту на латинський.
Замінює всі символи, крім латинських літер та цифр, на '_'.

Вимоги до функції normalize:

 - приймає на вхід рядок та повертає рядок;
 - проводить транслітерацію кириличних символів на латиницю;
 - замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
 - транслітерація може не відповідати стандарту, але бути читабельною;
 - великі літери залишаються великими, а маленькі — маленькими після транслітерації.

### Умови для обробки:

 - зображення переносимо до папки images
 - документи переносимо до папки documents
 - аудіо файли переносимо до audio
 - відео файли до video
 - архіви розпаковуються, та їх вміст переноситься до папки archives
 - файли з невідомими розширеннями скласти в папку other

### Критерії прийому завдання

 - всі файли перейменовуються за допомогою функції normalize.
 - розширення файлів не змінюється після перейменування.
 - порожні папки видаляються
 - скрипт ігнорує папки archives, video, audio, documents, images, others;
 - розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів, але без розширення у кінці. Зламані архіви, які не розпаковуються, треба видалити;

### В результатах роботи повинні бути:

 - Список файлів у кожній категорії (музика, відео, фото та ін.)
 - Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
 - Перелік всіх розширень, які скрипту невідомі.

Цей результат або вивести в консоль, або зберегти в файл.

### Файл результату: homework_6.py


## Homework 7 (Створення та встановлення власних пакетів)

### Завдання
У цьому домашньому завданні ми зробимо із скрипта розбору папки Python-пакет та консольний скрипт, який можна викликати у будь-якому місці системи з консолі командою clean-folder. Для цього вам треба створити структуру файлів та папок:

 ├── clean_folder
 │    ├── clean_folder
 │    │   ├── clean.py
 │    │   └── __init__.py
 │    └── setup.py


У clean_folder/clean_folder/clean.py треба помістити все, що ми зробили на попередніх домашніх завданнях по розбору папки. Ваше основнє завдання написати clean_folder/setup.py, щоб вбудований інструментарій Python міг встановити цей пакет та операційна система могла використати цей пакет як консольну команду.

### Критерії прийому завдання

 - Пакет встановлюється в систему командою pip install -e . (або python setup.py install, потрібні права адміністратора).
 - Після установки в системі з'являється пакет clean_folder.
 - Коли пакет встановлений в системі, скрипт можна викликати у будь-якому місці з консолі командою clean-folder
 - Консольний скрипт обробляє аргументи командного рядка точно так, як і Python-скрипт.

### Папка результату: homework_7