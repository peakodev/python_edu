import logging

# створюємо логер, даємо йому ім'я та встановлюємо рівень logging.DEBUG
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# створюємо handler для виведення в консоль та встановлюємо рівень DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# створюємо форматтер: час виведення (asctime), ім'я модуля (name), рівень (levelname) та саме повідомлення (message)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# додаємо зазначений форматтер до handler ch
ch.setFormatter(formatter)

# додаємо handler ch до логера
logger.addHandler(ch)

# Створюємо файловий handler для логера:
fh = logging.FileHandler("app.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)

# додаємо файловий handler fh до логера
logger.addHandler(fh)

# приклад виконання коду
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
